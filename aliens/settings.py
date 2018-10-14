############################################
###########################################
class Settings():
    """存储《外星人入侵》的所有设置的类"""
    def __init__(self):
        """初始化游戏的静态设置"""
        #屏幕设置
        self.screen_width  = 1200  #屏幕宽度
        self.screen_height = 800   #屏幕高度
        self.bg_color = (230,230,230) #屏幕内颜色RGB
        self.ship_limit = 3  #初始化游戏玩家飞船为3（三条命）
        
        #子弹（bullet）设置
        self.bullet_width = 10   #测试时可使用60的宽子弹
        self.bullet_height = 15
        self.bullet_color =60,60,60
        self.bullets_allowed = 6 #允许屏幕上存在的子弹数

        #外星人设置
        self.fleet_drop_speed = 20
        #以什么样的速度加快游戏节奏
        self.speedup_scale = 1.1
        #外星人点数的提高速度
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随着游戏进行而变化的设置"""
        self.ship_speed_factor = 1.5  #飞船左右移动速度
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        self.alien_points = 50

        #fleet_direction为1表示向右移动，为-1表示向左移动
        self.fleet_direction = 1

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        #print(self.alien_points)

