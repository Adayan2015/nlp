#-*-coding:UTF-8-*-
# 'ascii'
import requests

import pygal
from pygal.style import LightColorizedStyle, LightenStyle

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
response = requests.get(url)
print(response.status_code, '响应成功！')
response_dict = response.json()

total_repo = response_dict['total_count']
repo_list = response_dict['items']
print('总仓库数: ', total_repo)
print('top', len(repo_list))

names, plot_dicts = [], []
for repo_dict in repo_list:
	names.append(repo_dict['name'])
	# 加上str强转，因为我遇到了'NoneType' object is not subscriptable (: 说明里面有个没有此项, 是NoneType
	plot_dict = {'value': repo_dict['stargazers_count'], # 有些描述很长很长，选最前一部分
				'label':  str(repo_dict['description']),
				'xlink': repo_dict['html_url']}
	plot_dicts.append(plot_dict)

# 改变默认主题颜色，偏蓝色
my_style = LightenStyle('#333366', base_style=LightColorizedStyle)
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
chart.title = 'Most-Starred Python Projects on GitHub'
# x轴的数据
chart.x_labels = names
# 加入y轴的数据，无需title设置为空，注意这里传入的字典，
# 其中的键--value也就是y轴的坐标值了
chart.add('', plot_dicts)
chart.render_to_file('most_stars_python_repo.svg')