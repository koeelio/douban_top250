# -*- coding: utf-8 -*-
import scrapy
from apple.items import AppleItem

class NewsappleSpider(scrapy.Spider):
    name = "newsapple"
    # allowed_domains = ["hk.apple.nextmedia.com"]
    start_urls = ['http://hk.apple.nextmedia.com/realtime/realtimelist/top?page=top']


    def parse(self, response):
        items = AppleItem()

        lable = response.xpath("//div[@class='RTitem']")

        for i in lable:
            items['date']=i.xpath("div[@class='RTitemRHS']/div[@class='date']/text()").extract_first()
            items['time']=i.xpath("div[@class='RTitemRHS']/div[@class='time']/text()").extract_first()
            items['views']=i.xpath("div[@class='RTitemRHS']/div[@class='view02']/text()").extract_first()
            items['title']=i.xpath("div[@class='RTitemRHS']/div[@class='text']/a/text()").extract()[0]
            items['url']=i.xpath("div[@class='RTitemRHS']/div[@class='text']/a/@href").extract_first()

            yield items


