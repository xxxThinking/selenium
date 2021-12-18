'''
@File:test_addBug.py
@DateTime:17/12/2021 下午 8:20
@Author:sweet
@Desc:
'''
import time
import unittest

import win32con
import win32gui
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium_day05.config.config_1 import file,driver_file,url,sheet
from selenium_day05.data.testdata import ReadWrite
from selenium_day05.pageobjects.PageAddBug import AddBugPage

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        data_list = self.data.read()
        self.page = AddBugPage(self.driver)
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.click_login()

    @classmethod
    def setUpClass(cls) -> None:
        s = Service(driver_file)
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.get(url)
        cls.driver.maximize_window()
        cls.data = ReadWrite(file,sheet)
        cls.page = AddBugPage(cls.driver)

    # 跳过这个用例
    # @unittest.skip("该版本不需要执行")
    def test_addBug(self):

        self.driver.find_element(By.LINK_TEXT, "测试").click()
        self.driver.find_element(By.XPATH, "//nav[@id = 'subNavbar']/ul/li[1]/a").click()
        self.driver.find_element(By.LINK_TEXT, "提Bug").click()
        self.driver.find_element(By.CLASS_NAME, "chosen-choices").click()
        self.driver.find_element(By.CLASS_NAME, "active-result").click()
        self.driver.find_element(By.ID, "title").send_keys("test")
        # 分别类名查找肯定有一个是唯一指向
        self.driver.find_element(By.CLASS_NAME, "file-input-btn").click()

        time.sleep(1)
        # 1.查找
        # 编辑框
        # 一级窗口：参数（类名,title）
        dialog = win32gui.FindWindow("#32770", "打开")
        # 二级：FindWindowEx(子查找函数)参数(一级窗口,不点击就是0,类名,没有名字)
        combobox32 = win32gui.FindWindowEx(dialog, 0, "ComboBoxEx32", None)
        # 三级:同上一级
        combobox = win32gui.FindWindowEx(combobox32, 0, "ComboBox", None)
        # 四级
        edit = win32gui.FindWindowEx(combobox, 0, "Edit", None)

        # 查找按钮控件
        button = win32gui.FindWindowEx(dialog, 0, "Button", "打开(&O)")

        # 2.操作 往编辑当中,输入文件路径
        # 参数(编辑对象,使用方法,无多说明None/点击为1,文件路径)
        win32gui.SendMessage(edit, win32con.WM_SETTEXT, None, r"C:\Users\Administrator\Desktop\a.png")  # 发送文件路径
        win32gui.SendMessage(dialog, win32con.WM_COMMAND, 1, button)  # 点击打开按钮

        self.driver.find_element(By.ID, "submit").click()



    def tearDown(self) -> None:
        time.sleep(1)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()
