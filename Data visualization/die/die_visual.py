#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/12 星期日 19:52:31
# File Name: die_visual.py
# Description:
"""
import pygal
from die import Die

#创建一个D6

die_1 = Die()
die_2 = Die(10)
#多投几次色子，并将其存储在一个列表中
results = []
for roll_num in range(5000):
    result = die_1.roll() +die_2.roll()
    results.append(result)

#分析结果
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2 ,max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

#print(results)
#print(frequencies)
hist = pygal.Bar()

hist.title = "Results of rolling  D6 + D10 5000 times."
hist.x_labels = ['2','3','4','5','6','7','8','9','10','11','12','13','14','15','16']
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10' ,frequencies)
hist.render_to_file('die_visual.svg')
