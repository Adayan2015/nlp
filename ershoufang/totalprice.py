#-*-coding:UTF-8 -*-
import json
#解析json问题

#读取文件并解析为字典组成的列表
dicList=[json.load(line) for line in open('E:\PyCharm\PyCharmProjects\ershoufang\ershou.json')]
#打印第一个字典元素
print dicList[0]
#打印第一个元素中的时区
print dicList[0]['totalPrice']

#打印房屋信息和总体价格

	# print(price_data['totalPrice'])
	# print(price_data['url'])
	# print(price_data['region'])
	# print(price_data['attention'])
	# print(price_data['houseInfo'])
	# print(price_data['visited'])
	# print(price_data['unitPrice'])