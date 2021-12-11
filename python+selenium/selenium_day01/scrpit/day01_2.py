'''
@File:day01_2.py
@DateTime:2021/12/10 17:22
@Author:sweet
@Desc:
'''

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from data.testdata import ReadWrite
from config.config_1 import url,file,driver_file
from pageobjects.login_out import log_in_out

class TestLogCase:
    def test_1_login(self):
        content = ReadWrite(file,1)
        userlist = content.read()
        user = userlist[0]
        username = user[0]
        password = user[1]
        s = Service(driver_file)
        driver = webdriver.Chrome(service=s)
        driver.get(url)
        page = log_in_out(driver)
        if driver.title == "欢迎使用禅道集成运行环境":
            driver.find_element(By.ID,"zhentao").click()
        elif driver.title == "用户登录 - 禅道":
            page.input_username(username)
            time.sleep(4)
            page.input_password(password)
            try:
                page.click_login()
                time.sleep(4)
                alert = driver.switch_to.alert
                content = alert.text
                assert  '登录失败' in content
                print("用例成功。验证错误密码")
            except AssertionError:
                print("用例执行失败")

if __name__ == '__main__':
    case1 = TestLogCase()
    case1.test_1_login()