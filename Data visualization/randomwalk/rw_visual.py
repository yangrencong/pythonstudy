#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/12 星期日 11:24:15
# File Name: rw_visual.py
# Description:
"""
import matplotlib.pyplot as plt

from random_walk import RandomWalk

while True:
    #创建一个RandomWalk
    rw = RandomWalk()
    rw.fill_walk()
    
    #设置窗口绘制的尺寸
    plt.figure(figsize=(10 ,6))
    point_numbers = list(range(rw.num_points))

    #用线来描述并打印
    plt.plot(rw.x_values ,rw.y_values ,linewidth = 1)

    #用点打印
    #plt.scatter(rw.x_values ,rw.y_values ,c = point_numbers ,
    #        cmap = plt.cm.hsv ,edgecolor ='none' ,s =1)
    
    plt.axes().get_xaxis().set_visible(False)
    plt.axes().get_yaxis().set_visible(False)
    #突出起点和终点
    #plt.scatter(0 ,0 ,c='green' ,edgecolor = 'none' ,s=100)
    #plt.scatter(rw.x_values[-1] ,rw.y_values[-1] ,c='red',edgecolor = 'none',s=100)
    plt.show()
    
    keep_running = input("Make another walk ?(y/n)")
    if keep_running == 'n':
        break

