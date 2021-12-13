'''
@File:day04_unitest框架.py
@DateTime:2021/12/13 22:07
@Author:sweet
@Desc:
'''

import unittest

class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        print("登入禅道")

    @classmethod
    def setUpClass(cls) -> None:
        print("打开浏览器！")

    def test_adduser(self):
        print("执行添加用户用例")

    def test_deleteuser(self):
        print("执行删除用户用例")

    def tearDown(self) -> None:
        print("登出禅道")

    @classmethod
    def tearDownClass(cls) -> None:
        print("关闭浏览器！")

if __name__ == "__main__":
    # unittest.main
    unitest_suit=unittest.TestSuite()
    unitest_suit.addTest(TestCase("test_adduser"))
    unitest_suit.addTest(TestCase("test_deleteuser"))
    test_runner = unittest.TextTestRunner()
    test_runner.run()
