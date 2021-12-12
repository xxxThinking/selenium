'''
@File:day02_alert.py
@DateTime:2021/12/12 0:13
@Author:sweet
@Desc: 针对弹出窗口做处理
'''

from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert

from config.config_1 import file,url,driver_file


s = Service(driver_file)
driver = webdriver.Chrome(service=s)
driver.get(url)

driver.find_element(By.ID, "account").send_keys("")
driver.find_element(By.NAME, "password").send_keys("")
driver.find_element(By.ID, "submit").click()

# 调用方法定位alert
alert = Alert(driver)
# 用浏览器切换alert
alert = driver.switch_to.alert
# 获取弹窗得内容
values = alert.text
# 点击确定
alert.accept()
# 点击取消
alert.dismiss()