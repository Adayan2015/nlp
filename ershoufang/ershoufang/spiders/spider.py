#-*-coding:UTF-8-*-
import scrapy
from ershoufang.items import FangItem
from scrapy import Spider
#json字符串格式问题

class ershoufangSpider(scrapy.Spider):
	name = "ershoufangspider"
	start_urls = [
		"http://bj.lianjia.com/ershoufang/pg1",
		"http://bj.lianjia.com/ershoufang/pg2"

	]
	#解析数据
	def parse(self, response):
		items = []
		houses = response.xpath(".//ul[@class='sellListContent']/li")
		for house in houses:
			item = FangItem()
			item['houseInfo'] = house.xpath(".//div[@class='houseInfo']/text()").extract()
			item['totalPrice'] = house.xpath(".//div[@class='totalPrice']/span").re("\d+.\d+")
			item['attention'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[0]
			item['visited'] = house.xpath(".//div[@class='followInfo']/text()").re("\d+")[1]
			item['unitPrice'] = house.xpath(".//div[@class='unitPrice']/span").re("\d+.\d+")
			item['url'] = house.xpath(".//a[@class='img ']/@href").extract()
			item['region'] = house.xpath(".//div[@class='houseInfo']/a/text()").extract()
			items.append(item)
			items.append(",")
		return items