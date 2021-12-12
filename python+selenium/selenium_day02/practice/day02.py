'''
@File:day02.py
@DateTime:2021/12/11 2:11
@Author:sweet
@Desc: 将xlsx中数据用来登录注册 循环三次
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from config.config_1 import file,driver_file,url
from data.testdata import ReadWrite

# 读文件
l1 = ReadWrite(file,1)
userlist = l1.read()

s = Service(driver_file)
driver = webdriver.Chrome(service=s)
driver.get(url)
driver.maximize_window()

for i in range(0,3):
    driver.find_element(By.ID,"account").clear()
    driver.find_element(By.NAME,"password").clear()
    if driver.title == "用户登录 - 禅道":
        user = userlist[i]
        username = user[0]
        password = user[1]
        print(username,password)
        time.sleep(1)
        driver.find_element(By.ID,"account").send_keys(username)
        time.sleep(1)
        driver.find_element(By.NAME,"password").send_keys(password)
        time.sleep(1)
        driver.find_element(By.ID, "submit").click()
        time.sleep(2)
        try:
            try:
                alert = driver.switch_to.alert
                content = alert.text
                assert "登录失败" in content
                print("账号/密码错误登录失败用例,passed")
                driver.switch_to.alert.accept()
            except:
                # 自我标识
                driver.switch_to.alert.accept()
                print("failed--")
        except:
            if driver.title == "我的地盘 - 禅道":
                try:
                    print("测试登录成功用例,pass")
                    driver.find_element(By.CLASS_NAME,"user-name").click()
                    driver.find_element(By.LINK_TEXT,"退出").click()
                except:
                    alert = driver.switch_to.alert
                    content = alert.text
                    assert "登录失败" in content
                    print("failed--")

