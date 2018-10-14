#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/11 星期六 13:49:00
# File Name: scatter_squares.py
# Description:
"""
import matplotlib.pyplot as plt

x_values = list(range(1 ,5001))
y_values = [x**3 for x in x_values]

plt.scatter(x_values ,y_values ,c=y_values ,cmap = plt.cm.Blues ,edgecolor = 'none' ,s=40)

#设置图标标题，并给坐标轴加上标签
plt.title("Square Numbers" ,fontsize = 24)
plt.xlabel("Value" ,fontsize = 14)
plt.ylabel("Square of Value" ,fontsize = 14)

#设置每个坐标轴的取值范围
plt.axis([0 ,5100 ,0 ,5000**3])

#设置刻度标记的大小
plt.tick_params(axis = 'both' ,which = 'major' ,labelsize = 14)
plt.show()
plt.savefig('squares_plot.png' ,bbox_inches ='tight')

