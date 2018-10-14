#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/16 星期四 15:28:27
# File Name: bar_descriptions.py
# Description:
"""
import pygal
from pygal.style import LightColorizedStyle as LCS ,LightenStyle as LS

my_style = LS('#333366' ,base_style = LCS)
chart = pygal.Bar(style = my_style ,x_label_rotation = 45 ,show_legend = False)

chart.title = 'Python Project'
chart.x_labels = ['httpie' ,'django' ,'flask']
plot_dicts = [
        {'value':16101 ,'label':'Description of httpie'},
        {'value':15028 ,'label':'Description of django'},
        {'value':14798 ,'label':'Description of flask'}
        ]

chart.add('' ,plot_dicts)
chart.render_to_file('bar_description.svg')

