#-*-coding:UTF-8 -*-
import json
import matplotlib.pyplot as plt
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

#将数据加载到一个列表中
filename = 'ershoufang.json'
with open(filename) as f:
	pop_data = json.load(f)

#获取户型
housetype = []
for fang_dict in pop_data:
	houseinfo = fang_dict['houseInfo'][0]
	w = houseinfo.split('|')[1].encode('UTF-8')
	print(w)
	housetype.append(w)

myhouse = set(housetype)
housetypenum = []
for i in myhouse:
	housetypenum.append(housetype.count(i))

sp =flgure
plt.bar(range(len(housetypenum)),housetypenum,fc='r',tick_label=myhouse)
plt.show()