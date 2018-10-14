#!/usr/bin/env python
# -*- coding=utf8 -*-
"""
# Author: Mr.yang
# Created Time : 2018/8/8 星期三 12:50:08
# File Name: game_stats.py
# Description:
"""
import json

class GameStats():
    #跟踪游戏统计信息
    
    def __init__(self ,ai_settings):
        #初始化统计信息
        self.ai_settings = ai_settings
        self.reset_stats()
        #游戏刚启动时处于活动状态
        self.game_active = False
        #在任何时候都不重置最高分
        filename = 'high_score.json'
        try:
            with open(filename) as f_obj:
                self.high_score = json.load(f_obj)
        except FileNotFoundError:
            self.high_score = 0
            with open(filename ,'w') as f_obj:
                json.dump(self.high_score ,f_obj)
                print("ok")

    def reset_stats(self):
        #初始化在游戏运行过程中可能变化的统计信息
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1

