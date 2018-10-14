########################
########################
from random import randint

class Die():
    """表示一个色子的类"""

    def __init__(self ,num_sides = 6):
        """默认色子有六个面"""
        self.num_sides = num_sides

    def roll(self):
        """返回一个位于1和色子面数上的随机数"""
        return randint(1 ,self.num_sides)
