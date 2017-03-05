# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AppleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    date = scrapy.Field()
    time = scrapy.Field()
    title = scrapy.Field()
    views = scrapy.Field()
    url = scrapy.Field()

class DoubanItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    des = scrapy.Field()
    rating = scrapy.Field()
    item_url = scrapy.Field()
    comment = scrapy.Field()
    inq = scrapy.Field()
    url = scrapy.Field()
    movie_time = scrapy.Field()

    images = scrapy.Field()
    location = scrapy.Field()

    main_url = scrapy.Field()
    project = scrapy.Field()
    spider = scrapy.Field()
    server = scrapy.Field()
    date = scrapy.Field()
