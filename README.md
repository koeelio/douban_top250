# douban电影Top250_Scrapy_

- Python 3.5x
- Scrapy 1.21


## 使用Scrapy自带的cmdline类，写了一个main.py
该文件代码只有两行，只是为了方便测试代码，不需要每次到terminal下输入命令，只要在pycharm上设置的运行设置上配置好文件路径

	from scrapy import cmdline
	cmdline.execute('scrapy crawl doubantop250'.split())

在pycharm下运行设置需要注意：
- 在script下设置main.py的路径
- Working directory下设置项目所在位置，否则pycharm无法识别在哪个文件路径运行以上代码
## remind
因为douban设置了访问头验证，所以需要设置头部信息
所以在setting.py上面设置了

	DEFAULT_REQUEST_HEADERS = {
	  'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	  'Accept-Language': 'en',
	'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
	}

这样每次request就会带上header信息去访问网页

## 网页解析
使用的是Scrapy自带的selector，用的是Xpath
在返回items的时候用到了Scrapy的ItemLoder这个类
ItemLoder这个类的作用是让爬取的数据格式化，可以自定义格式。
使用时需要先实例化这个类，
	l = ItemLoader(DoubanItem(), response)

第一个参数是我们定义的item，第二个参数是爬取网页的response

接下来就可以用实例方法add\_xpath或add\_css来归类，定义item里面的内容。
例如：

	l.add_xpath('title',
	'div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()',
	MapCompose(lambda i: i.replace('\xa0', '')), Join(), )


第一个参数，是我们定义的item类里面的key，
第二个参数是我们指定的某一个爬取内容，
后续参数主要是有两个类，一个是Join()这个类可以把访问内容结合在一个字段，不需要做额外的处理，另一个是MapCompose()，这个类接受的参数为函数，所以这里可以使用lambda函数，定义我们需要格式化的逻辑。另外我们经常遇到一些换行符。也可以在MapCompose()里传入str.strip这个函数，可去除一些换行和空格。
最后add\_xpath这个类方法，还接受一个参数，re=
re顾名思义就是正则表达式。
是的，我们还可以通过re自定义需要自己的想要返回的数据。
非常方便。
## 最后再介绍一下定义的item类。
为了让数据呈现的更加规范,还多添加了5个字段：


	    main_url = scrapy.Field() #爬虫的网址
	    project = scrapy.Field() #爬虫的项目名称
	    spider = scrapy.Field() #爬虫的名称
	    server = scrapy.Field() #爬虫所运行的server
	    date = scrapy.Field() #数据添加的时间



这样可以让数据更具体的呈现
所以在爬虫的解析中返回item时也需要添加这个几个字段的信息


		l.add_value('main_url', response.url)
		l.add_value('project', self.settings.get('BOT_NAME'))
	        l.add_value('spider', self.name)
		l.add_value('server', socket.gethostname())
		l.add_value('date',''.join(str(datetime.datetime.now())))



最后，

	        yield l.load_item()










