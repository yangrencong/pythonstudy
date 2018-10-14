############################################
################2018年8月10日完成###########
############################################
"""/** 
*　　　　　　　　┏┓　　　┏┓+ + 
*　　　　　　　┏┛┻━━━┛┻┓ + + 
*　　　　　　　┃　　　　　　　┃ 　 
*　　　　　　　┃　　　━　　　┃ ++ + + + 
*　　　　　　 ████━████ ┃+ 
*　　　　　　　┃　　　　　　　┃ + 
*　　　　　　　┃　　　┻　　　┃ 
*　　　　　　　┃　　　　　　　┃ + + 
*　　　　　　　┗━┓　　　┏━┛ 
*　　　　　　　　　┃　　　┃　　　　　　　　　　　 
*　　　　　　　　　┃　　　┃ + + + + 
*　　　　　　　　　┃　　　┃　　　　Code is far away from bug with 　　　　　　 
*　　　　　　　　　┃　　　┃ + 　　　the animal protecting !　　　 
*　　　　　　　　　┃　　　┃         　神兽保佑,代码无bug !
*　　　　　　　　　┃　　　┃　　+　　　　　　　　　 
*　　　　　　　　　┃　 　　┗━━━┓ + + 
*　　　　　　　　　┃ 　　　　　　　┣┓# 
*　　　　　　　　　┃ 　　　　　　　┏┛ #
*　　　　　　　　　┗┓┓┏━┳┓┏┛ + + + +   #
*　　　　　　　　　　┃┫┫　┃┫┫ 
*　　　　　　　　　　┗┻┛　┗┻┛+ + + + 
*/"""
import sys
import pygame
from settings import Settings
from ship import Ship
from pygame.sprite import Group
from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
import game_function as gf

def run_game():
    #初始化游戏并创建一屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(( ai_settings.screen_width ,
                                       ai_settings.screen_height ))
    pygame.display.set_caption("Alien Invasion by Mr.yang")
    #创建Play按钮
    play_button = Button(ai_settings ,screen ,"Play")
    #创建一个用于统计游戏信息的实例
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings ,screen ,stats)    
    ship = Ship(ai_settings,screen)
    #创建一个存储子弹的编组
    bullets = Group()
    #创建外星人群
    aliens = Group()
    gf.create_fleet(ai_settings ,screen ,ship ,aliens)
  
    #开始游戏的主循环
    while True:

        gf.check_events(ai_settings ,screen ,stats ,sb ,play_button ,ship ,aliens ,bullets)
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings ,screen ,stats ,sb ,ship ,aliens ,bullets)
            gf.update_aliens(ai_settings ,screen ,stats ,sb ,ship ,aliens ,bullets)
        gf.update_screen(ai_settings ,screen ,stats ,sb ,ship ,aliens, bullets ,play_button)

run_game()
