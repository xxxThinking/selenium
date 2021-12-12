'''
@File:day02_3.py
@DateTime:2021/12/11 22:04
@Author:sweet
@Desc:鼠标操作
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from config.config_1 import file,url,driver_file
from selenium.webdriver.common.action_chains import ActionChains

s = Service(driver_file)
driver = webdriver.Chrome(service=s)
driver.get("https://www.baidu.com")
driver.maximize_window()
time.sleep(3)
# 一个class可以有多个类名用空格隔开 但有唯一标识得类名
# target_elem = driver.find_element(By.ID,"s-usersetting-top")
target_elem = driver.find_element(By.CLASS_NAME,"s-top-right-text")
ActionChains(driver).move_to_element(target_elem).perform()
