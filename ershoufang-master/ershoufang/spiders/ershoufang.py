 #-*- coding: utf-8 -*-
import scrapy
import re
from ershoufang.items import ErshoufangItem

class ershoufangSpider(scrapy.Spider):
    name = "ershoufang"
    start_urls = ["http://bj.lianjia.com/ershoufang/pg1"]

    def parse(self, response):
        items = []
        houses = response.xpath(".//ul[@class='sellListContent']/li")
        for house in houses:
            item = ErshoufangItem()
            item['houseInfo'] = house.xpath(".//div[@class='houseInfo']/text()").extract()
            item['totalPrice'] = house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+")
            item['attention'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
            item['visited'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
            item['unitPrice'] = house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+")
            item['url'] = house.xpath(".//a[@class='img ']/@href").extract()
            item['region'] = house.xpath(".//div[@class='houseInfo']/a/text()").extract()
            items.append(item)
            yield item
        #翻页
        page = response.xpath("//div[@class='page-box house-lst-page-box'][@page-data]").re("\d+")
        print page + "-----------------------------------"
        p = re.compile(r'[^\d]+')
        if len(page)>1 and page[0] != page[1]:
            next_page = p.match(response.url).group()+str(int(page[1])+1)
            print next_page+"*********************"
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)
