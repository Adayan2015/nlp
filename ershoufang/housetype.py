#-*-coding:UTF-8 -*-
import json
import  re
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#解析json问题

#将数据加载到一个列表中
filename = 'ershoufang.json'
with open(filename) as f:
	pop_data = json.load(f)

#获取户型
housetype = []
for fang_dict in pop_data:
	#houseinfo = fang_dict['houseInfo'][0].encode('unicode-escape').decode('string_escape')
	houseinfo = fang_dict['houseInfo'][0]
	w = houseinfo.split('|')[1]
	housetype.append(w)

myhouse = set(housetype)
housetypenum = []
for i in myhouse:
	housetypenum.append(housetype.count(i))

#可视化
# 改变默认主题颜色，偏蓝色
my_style = LS('#FF3300', base_style=LCS)
# 配置
my_config = pygal.Config()
# x轴的文字旋转45度
my_config.x_label_rotation = -45
# 隐藏左上角的图例
my_config.show_legend = False
# 标题字体大小
my_config.title_font_size = 36
# 副标签，包括x轴和y轴大部分
my_config.label_font_size = 20
# 主标签是y轴某数倍数，相当于一个特殊的刻度，让关键数据点更醒目
my_config.major_label_font_size = 24
# 限制字符为15个，超出的以...显示
my_config.truncate_label = 15
# 不显示y参考虚线
my_config.show_y_guides = False
# 图表宽度
my_config.width = 1000

# 第一个参数可以传配置
chart = pygal.Bar(my_config, style=my_style)
chart.title = 'Type distribution Lian Jia ershoufang'
# x轴的数据
chart.x_labels = myhouse
chart.x_title = "House type"
chart.y_title = "Number"
# 加入y轴的数据，无需title设置为空，注意这里传入的字典，
# 其中的键--value也就是y轴的坐标值了
chart.add('户型套数：', housetypenum)
chart.render_to_file('lianjiafang.svg')