import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):#创建新的bullet类，并继承sprite
    def __init__(self ,ai_settings ,screen ,ship ):
        """在飞船的位置在创建一个子弹对象"""
        super(Bullet ,self).__init__() #让bullet继承sprite的所有属性
        self.screen = screen

        #在（0,0）处创建一个表示子弹的矩形，在设置其位置
        self.rect = pygame.Rect(0 ,0 ,ai_settings.bullet_width,
                                ai_settings.bullet_height )
        self.rect.centerx = ship.rect.centerx
        self.rect.top = ship.rect.top
        #存储用小数表示的子弹位置
        self.y = float(self.rect.y)
        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹"""
        #更新表示子弹位置的小数值
        self.y -= self.speed_factor
        #更新表示子弹的rect位置
        self.rect.y = self.y


    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen ,self.color ,self.rect)
        
      
