'''
@File:day01_3.py
@DateTime:2021/12/16 16:39
@Author:sweet
@Desc:
'''

from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

s = Service("G:\selenium\OfficeUpdate.exe\python+selenium\driver\chrome96.0.4664.93 96.0.4664.45\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("file:///C:/Users/Administrator/Desktop/%E6%96%B0%E5%BB%BA%E6%96%87%E6%9C%AC%E6%96%87%E6%A1%A3.html")

# getElement
# js = "document.getElementById('yoyoketang').scrollTop=1000"
# driver.execute_script(js)
#
# js1 = "document.getElementById('yoyoketang').scrollLeft=1000"
# driver.execute_script(js1)


# elements
js = "document.getElementsByClassName('scroll')[0].scrollTop=1000"
driver.execute_script(js)

js1 = "document.getElementsByClassName('scroll')[0].scrollLeft=1000"
driver.execute_script(js1)