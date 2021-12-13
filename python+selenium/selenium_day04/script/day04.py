'''
@File:day04.py
@DateTime:2021/12/13 21:19
@Author:sweet
@Desc: css练习
'''

# 查找元素
from time import sleep

import win32gui
# 元素操作
import win32con

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

from config.config_1 import file,url,driver_file



s = Service(driver_file)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()


driver.find_element(By.CSS_SELECTOR, "#account").send_keys("shelly")
driver.find_element(By.XPATH, "//*[@name = 'password']").send_keys("p@ssw0rd")
driver.find_element(By.CSS_SELECTOR, "td button").click()
# driver.find_element(By.CSS_SELECTOR, ".form-actions :nth-child(1)").click()