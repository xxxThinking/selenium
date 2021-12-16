'''
@File:test_login.py
@DateTime:2021/12/15 22:00
@Author:sweet
@Desc:
'''
'''
@File:day04_uni.py
@DateTime:2021/12/14 13:54
@Author:sweet
@Desc:
'''
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config.config_1 import file,driver_file,url

class TestCases(unittest.TestCase):
    def setUp(self) -> None:
        s = Service(driver_file)
        self.driver = webdriver.Chrome(service=s)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.driver.maximize_window()

    @classmethod
    def setUpClass(cls) -> None:
        pass

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "user-name").click()
        self.driver.find_element(By.LINK_TEXT, "退出").click()

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test_login(self):
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()

