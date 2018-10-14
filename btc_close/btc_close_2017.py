#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/13 星期一 20:03:09
# File Name: btc_close_2017.py
# Description:
"""
import json
import pygal
from itertools import groupby
import math
#创建五个列表，将数据加载到列表里


file_name = 'btc_close_2017.json'
with open(file_name) as f_obj:
    btc_data = json.load(f_obj)

# 打印每一天的信息
for btc_dict in btc_data:
    date = btc_dict['date']
    month = int(btc_dict['month'])
    week = int(btc_dict['week'])
    weekday = btc_dict['weekday']
    close = int(float(btc_dict['close']))  # 1
    print("{} is month {} week {}, {}, the close price is {} RMB".format(
        date, month, week, weekday, close))

dates = []
months = []
weeks = []
weekdays = []
close = []
# 每一天的信息
for btc_dict in btc_data:
    dates.append(btc_dict['date'])
    months.append(int(btc_dict['month']))
    weeks.append(int(btc_dict['week']))
    weekdays.append(btc_dict['weekday'])
    close.append(int(float(btc_dict['close'])))


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)  # ①
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
N = 20  # x轴坐标每隔20天显示一次
line_chart.x_labels_major = dates[::N]  # ②
line_chart.add('收盘价', close)
line_chart.render_to_file('收盘价折线图（¥）.svg')

line_chart = pygal.Line(x_label_rotation = 20 ,show_minor_x_labels = False)
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
N = 20 #坐标轴每隔20天显示一次
line_chart.x_labels_major = dates[ : :N]
close_log = [math.log10(d) for d in close]
line_chart.add('log收盘价' ,close_log)
line_chart.render_to_file('收盘价对数变换折线图（¥）.svg')

def draw_line(x_data, y_data, title, y_legend):
    xy_map = []
    for x, y in groupby(sorted(zip(x_data, y_data)), key=lambda _: _[0]):  # 2
        y_list = [v for _, v in y]
        xy_map.append([x, sum(y_list) / len(y_list)])  # 3
    x_unique, y_mean = [*zip(*xy_map)]  # 4
    line_chart = pygal.Line()
    line_chart.title = title
    line_chart.x_labels = x_unique
    line_chart.add(y_legend, y_mean)
    line_chart.render_to_file(title + '.svg')
    return line_chart


idx_month = dates.index('2017-12-01')
line_chart_month = draw_line(
        months[:idx_month], close[:idx_month], '收盘价月日均值（¥）', '月日均值')
line_chart_month



