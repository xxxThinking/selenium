'''
@File:test_login.py
@DateTime:2021/12/15 22:00
@Author:sweet
@Desc:
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from selenium_day05.config.config_1 import file,driver_file,url,sheet
from selenium_day05.data.testdata import ReadWrite
from selenium_day05.pageobjects.Pagelogin import Loginpage
from selenium_day05.log.log import logger

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        self.doc1 = ReadWrite(file,sheet)
        self.page = Loginpage(self.driver)

    @classmethod
    def setUpClass(cls) -> None:
        s = Service(driver_file)
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.get(url)
        cls.driver.maximize_window()

    def tearDown(self) -> None:
        self.driver.find_element(By.ID, "account").clear()
        self.driver.find_element(By.NAME, "password").clear()

    @classmethod
    def tearDownClass(cls) -> None:
        cls.driver.quit()

    def testA_login(self):
        '''登陆成功用例'''
        data_list = self.doc1.read()
        self.page.type_username(data_list[0][0])
        self.page.type_password(data_list[0][1])
        self.page.cilck_login()
        time.sleep(1)
        self.assertEqual(self.driver.title,"我的地盘 - 禅道")
        self.page.click_logout()

    def testB_login_ErrorPassword(self):
        '''密码错误用例'''
        data_list = self.doc1.read()
        self.page.type_username(data_list[1][0])
        self.page.type_password(data_list[1][1])
        self.page.cilck_login()
        time.sleep(1)
        content = self.driver.switch_to.alert
        self.assertIn("登录失败", content.text)
        # 添加日志
        # logger.info("验证用户登录成功信息")
        content.accept()

    def testC_login_ErrorAdmin(self):
        '''不存在用户名用例'''
        data_list = self.doc1.read()
        self.page.type_username(data_list[2][0])
        self.page.type_password(data_list[2][1])
        self.page.cilck_login()
        time.sleep(1)
        content = self.driver.switch_to.alert
        self.assertIn("登录失败", content.text)
        content.accept()

    def testD_login_Blank(self):
        '''不输入用户名密码用例'''
        self.page.cilck_login()
        time.sleep(1)
        content = self.driver.switch_to.alert
        self.assertIn("登录失败",content.text)
        content.accept()


