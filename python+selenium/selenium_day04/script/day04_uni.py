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

class Case1(unittest.TestCase):
    def setUp(self) -> None:
        self.driver.find_element(By.ID, "account").send_keys("shelly")
        self.driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()

        self.driver.find_element(By.LINK_TEXT, "组织").click()

    @classmethod
    def setUpClass(cls) -> None:
        s = Service(driver_file)
        cls.driver = webdriver.Chrome(service=s)
        cls.driver.implicitly_wait(10)
        cls.driver.get(url)
        cls.driver.maximize_window()

    def tearDown(self) -> None:
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "user-name").click()
        self.driver.find_element(By.LINK_TEXT, "退出").click()

    @classmethod
    def tearDownClass(cls) -> None:
        time.sleep(1)
        cls.driver.quit()

    def test_add(self):
        self.driver.find_element(By.LINK_TEXT, "添加用户").click()

        self.driver.find_element(By.ID, "account").send_keys("shelly19")
        self.driver.find_element(By.NAME, "password1").send_keys("p@ssw0rd")
        self.driver.find_element(By.NAME, "password2").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "realname").send_keys("shelly19")

        # 下拉框
        select_element = self.driver.find_element(By.ID, "role")
        Select(select_element).select_by_visible_text("测试主管")

        self.driver.find_element(By.NAME, "verifyPassword").send_keys("p@ssw0rd")

        # 利用javascript脚本写滚动条
        js = "document.documentElement.scrollTop = 1000"
        self.driver.execute_script(js)

        self.driver.find_element(By.ID, "submit").click()

        self.driver.find_element(By.LINK_TEXT, "用户").click()
        self.driver.find_element(By.ID, "bysearchTab").click()
        self.driver.find_element(By.ID, "value1").send_keys("shelly19")
        self.driver.find_element(By.ID, "submit").click()

    def test_delte(self):
        self.driver.find_element(By.ID, "bysearchTab").click()
        self.driver.find_element(By.ID, "value1").send_keys("shelly19")
        self.driver.find_element(By.ID, "submit").click()

        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, "icon-trash").click()
        self.driver.switch_to.frame("iframe-triggerModal")
        self.driver.find_element(By.NAME, "verifyPassword").send_keys("p@ssw0rd")
        self.driver.find_element(By.ID, "submit").click()

        time.sleep(1)
        self.driver.switch_to.default_content()
        self.driver.find_element(By.ID, "submit").click()

if __name__=="__main__":
    # unittest.main()
    suit = unittest.TestSuite()
    suit.addTest(Case1("test_add"))
    runner = unittest.TextTestRunner()
    runner.run(suit)