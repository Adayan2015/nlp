# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ErshoufangItem(scrapy.Item):
    # define the fields for your item here like:
    houseInfo = scrapy.Field()
    totalPrice = scrapy.Field()
    attention = scrapy.Field()
    visited = scrapy.Field()
    unitPrice = scrapy.Field()
    url = scrapy.Field()
    region = scrapy.Field()
    pass
