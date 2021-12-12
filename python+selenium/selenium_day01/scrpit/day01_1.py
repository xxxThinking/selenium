'''
@File:day01_1.py
@DateTime:2021/12/10 0:09
@Author:sweet
@Desc:
'''

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("G:\selenium\OfficeUpdate.exe\python+selenium\driver\chrome96.0.4664.93 96.0.4664.45\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
if driver.title == "欢迎使用禅道集成运行环境":
    driver.find_element(By.ID,"zhentao").click()
elif driver.title == "用户登录 - 禅道":
    driver.find_element(By.ID,"account").send_keys('shelly')
    time.sleep(4)
    driver.find_element(By.NAME,"password").send_keys('p@ssw0rd')
    try:
        driver.find_element(By.ID,"submit").click()
        time.sleep(4)
        alert = driver.switch_to.alert
        content = alert.text
        assert  '登录失败' in content
        print("用例成功。验证错误密码")
    except AssertionError:
        print("用例执行失败")
