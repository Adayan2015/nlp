#-*-coding:UTF-8 -*-
import json
import pygal
from pygal.style import LightColorizedStyle as LCS,LightenStyle as LS
#解析json问题

#将数据加载到一个列表中
filename = 'ershoufang.json'
with open(filename) as f:
	pop_data = json.load(f)

#打印房屋信息和总体价格
regions,plot_dicts = [],[]
for fang_dict in pop_data:
	regions.append(fang_dict['region'][0])
	plot_dict = {'value': int(fang_dict['totalPrice'][0]),
		'label': fang_dict['houseInfo'][0], 'xlink': fang_dict['url'][0]}
	plot_dicts.append(plot_dict)
#可视化
# 改变默认主题颜色，偏蓝色
my_style = LS('#333366', base_style=LCS)
# 配置
my_config = pygal.Config()
# x轴的文字旋转45度
my_config.x_label_rotation = -45
# 隐藏左上角的图例
my_config.show_legend = False
# 标题字体大小
my_config.title_font_size = 30
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
chart.title = 'Lian Jia ershoufang'
# x轴的数据
chart.x_labels = regions
# 加入y轴的数据，无需title设置为空，注意这里传入的字典，
# 其中的键--value也就是y轴的坐标值了
chart.add('', plot_dicts)
chart.render_to_file('lianjia.svg')