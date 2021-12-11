'''
@File:day01.py
@DateTime:2021/12/8 22:09
@Author:sweet
@Desc:
'''

# chrome
from selenium import webdriver
import time
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

s = Service("G:\python+selenium\driver\chrome96.0.4664.93 96.0.4664.45\chromedriver.exe")
driver = webdriver.Chrome(service=s)
driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")
# 1.
# driver.find_element(By.ID,"account").send_keys("shelly")
# driver.find_element(By.NAME,"password").send_keys("p@ssw0rd")
# driver.find_element(By.ID,"submit").click()
# time.sleep(2)
# try:
#     assert driver.title == "我的地盘 - 禅道"
#     print("passed")
# except:
#     print("failed")
# driver.close()

# 2.添加窗口
# 当前窗口句柄
current_handle = driver.current_window_handle
print(current_handle)
js = 'window.open("https://www.baidu.com");'
driver.execute_script(js)

# 3.切换窗体回原窗口
# 句柄类似于计算机中一种标识 可能是虚拟地址
# 显示所有窗口句柄
handles = driver.window_handles
print(handles)
driver.switch_to.window(handles[0])

# driver.set_window_size(20,200)
# # 4.后退
# driver.back()
# # 刷新
# driver.refresh()
# # 前进
# driver.forward()
# 输入后清除
# driver.find_element(By.ID,"account").send_keys("asdase")
# time.sleep(2)
# driver.find_element(By.ID,"account").clear()
# 关闭全部
# driver.quit()
# 关闭当前所在
driver.close()


# egd
# from selenium import webdriver
# from selenium.webdriver.edge.service import Service
#
# s = Service("G:\python+selenium\driver\ege96.0.1054.43 96.0.1054.43\msedgedriver.exe")
# driver = webdriver.Edge(service=s)
# driver.get("http://139.224.113.59/zentao/user-login-L3plbnRhby8=.html")

# firefox
# from selenium import webdriver
# from selenium.webdriver.firefox.service import Service
#
# s = Service(r"G:\python+selenium\driver\friefox95.0_0.30\geckodriver.exe")
# driver = webdriver.Firefox(service=s)
# driver.get("http://ww.baidu.com")
# driver.maximize_window()