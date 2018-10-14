import unittest
from name_function import get_formatted_name

class NameTestCase(unittest.TestCase):
    """测试name_function.py"""

    def test_first_last_name(self):
        """能够正确的处理Jains Joplin这样的姓名吗？"""
        formatted_name = get_formatted_name("jains","joplin")
        self.assertEqual(formatted_name ,"Jains Joplin")

    def test_first_last_middle_name(self):
        """能够正确的处理yang ren cong这样的姓名吗?"""
        formatted_name = get_formatted_name("yang","cong","ren")
        self.assertEqual(formatted_name ,"Yang Ren Cong")

unittest.main()

