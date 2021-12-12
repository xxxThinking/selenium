'''
@File:day03_1.py
@DateTime:2021/12/12 23:53
@Author:sweet
@Desc: 上传元素的运用
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


driver.find_element(By.ID, "account").send_keys("shelly")
driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
driver.find_element(By.ID, "submit").click()

driver.find_element(By.LINK_TEXT,"测试").click()
driver.find_element(By.XPATH,"//nav[@id = 'subNavbar']/ul/li[1]/a").click()
driver.find_element(By.LINK_TEXT,"提Bug").click()
driver.find_element(By.CLASS_NAME,"chosen-choices").click()
driver.find_element(By.CLASS_NAME,"active-result").click()
driver.find_element(By.ID,"title").send_keys("test")
#分别类名查找肯定有一个是唯一指向
driver.find_element(By.CLASS_NAME,"file-input-btn").click()

sleep(1)
# 1.查找
# 编辑框
# 一级窗口：参数（类名,title）
dialog  = win32gui.FindWindow("#32770","打开")
# 二级：FindWindowEx(子查找函数)参数(一级窗口,不点击就是0,类名,没有名字)
combobox32 = win32gui.FindWindowEx(dialog,0,"ComboBoxEx32",None)
# 三级:同上一级
combobox = win32gui.FindWindowEx(combobox32,0,"ComboBox",None)
# 四级
edit = win32gui.FindWindowEx(combobox,0,"Edit",None)

# 查找按钮控件
button = win32gui.FindWindowEx(dialog,0,"Button","打开(&O)")

# 2.操作 往编辑当中,输入文件路径
# 参数(编辑对象,使用方法,无多说明None/点击为1,文件路径)
win32gui.SendMessage(edit,win32con.WM_SETTEXT,None,r"C:\Users\Administrator\Desktop\a.png") #发送文件路径
win32gui.SendMessage(dialog,win32con.WM_COMMAND,1,button)  #点击打开按钮


driver.find_element(By.ID,"submit").click()

