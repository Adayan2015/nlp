 #-*- coding: utf-8 -*-
import scrapy
from ershoufang.items import ErShouFangItem

class ershoufangSpider(scrapy.Spider):
    name = "ershoufangspider"
    start_urls = ["http://bj.lianjia.com/ershoufang/pg1"]

    def parse(self, response):
        items = []
        houses = response.xpath("//ul[@class='sellListContent']//li[@class='clear']")
        for house in houses:
            item = ErShouFangItem()
            item['totalPrice'] = house.xpath("./div/div[4]/div/div[@class='totalPrice']/span").re("\d+.\d+")[0]
            item['houseInfo'] = house.xpath("./div/div[2]/div[@class='houseInfo']/text()").extract()
            item['housetype'] = house.xpath("./div/div[2]/div[@class='houseInfo']/text()").extract()[0]
            item['housearea'] = house.xpath("./div/div[2]/div[@class='houseInfo']/text()").extract()[1]
            item['decoration'] = house.xpath("./div/div[2]/div[@class='houseInfo']/text()").extract()[3]
            item['attention'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
            item['visited'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
            item['unitPrice'] = house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+")[0]
            item['url'] = house.xpath(".//a[@class='img ']/@href").extract()[0]
            item['region'] = house.xpath(".//div[@class='houseInfo']/a/text()").extract()[0]
            items.append(item)
        return items