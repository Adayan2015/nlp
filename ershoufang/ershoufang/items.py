# -*- coding: utf-8 -*-
import scrapy

class FangItem(scrapy.Item):
    # define the fields for your item here like:
    houseInfo = scrapy.Field()
    totalPrice = scrapy.Field()
    attention = scrapy.Field()
    visited = scrapy.Field()
    unitPrice = scrapy.Field()
    url = scrapy.Field()
    region = scrapy.Field()

