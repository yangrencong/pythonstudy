import pygame
from pygame.sprite import Sprite

class Ship(Sprite):

    def __init__(self,ai_settings,screen):
        """初始化飞船并设置其初始位置"""
        super(Ship ,self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load(
                "C:/Users/Administrator/Desktop/python_s/aliens/images/ship.bmp")
        self.rect = self.image.get_rect()  #图像rect
        self.screen_rect = screen.get_rect()  #屏幕rect

        #将每艘飞船放在屏幕中央(处理外接矩形)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom  = self.screen_rect.bottom
        
        #将飞船的centerx属性存入一个float数据中
        self.centerx = float(self.rect.centerx)

        #移动标志位
        self.moving_right = False
        self.moving_left = False

    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image, self.rect)

    #关于按下不松，飞船连续移动
    def update(self):
        """根据移动标志调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.centerx -= self.ai_settings.ship_speed_factor

        #将self.centerx更新到self.rect.centerx
        self.rect.centerx = self.centerx
    
    def center_ship(self):
        #让飞船在屏幕中居中
        self.center = self.screen_rect.centerx



            
