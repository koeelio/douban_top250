# -*- coding: utf-8 -*-
import datetime
import socket

import scrapy
from scrapy import Request
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, Join

from apple.items import DoubanItem


class Doubantop250Spider(scrapy.Spider):
    name = "doubantop250"
    # allowed_domains = ["https://movie.douban.com/top250"]
    start_urls = ['https://movie.douban.com/top250']

    def parse(self, response):
        # a = response.xpath('//div[@class="paginator"]/a[contains(@href,"start")]/@href').extract()
        # for url in a:
        #     urls = response.urljoin(url)
        #     yield Request(urls,callback=self.parse_item)
        all = response.xpath('//div[@class="item"]')

        for i in all:
            l = ItemLoader(DoubanItem(), i)
            l.add_xpath('title',
                        'div[@class="info"]/div[@class="hd"]/a/span[@class="title"]/text()',
                        MapCompose(lambda i: i.replace('\xa0', '')), Join(), )
            l.add_xpath('des', 'div[@class="info"]/div[@class="bd"]/p/text()',
                        MapCompose(lambda i: i.replace('\xa0', ' '), str.strip),
                        Join())
            l.add_xpath('movie_time', 'div[@class="info"]/div[@class="bd"]/p/text()',re='\d{4}',)
            l.add_xpath('rating',
                        'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()',
                        MapCompose(str.strip))
            l.add_xpath('comment',
                        'div[@class="info"]/div[@class="bd"]/div[@class="star"]/span[4]/text()',
                        re='\d+')
            l.add_xpath('inq',
                        'div[@class="info"]/div[@class="bd"]/p[@class="quote"]/span[@class="inq"]/text()')
            l.add_xpath('url',
                        'div[@class="info"]/div[@class="hd"]/a/@href')

            l.add_value('main_url', response.url)
            l.add_value('project', self.settings.get('BOT_NAME'))
            l.add_value('spider', self.name)
            l.add_value('server', socket.gethostname())
            l.add_value('date', ''.join(str(datetime.datetime.now())))
            yield l.load_item()
        next_url = response.xpath('//link[contains(@rel,"next")]/@href').extract()
        if next_url:
            next_url = next_url[0]
            yield Request(response.urljoin(next_url))
