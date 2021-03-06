'''
@File:day02_1.py
@DateTime:2021/12/11 18:39
@Author:sweet
@Desc: 添加用户-删除用户-再点击搜索验证
隐式等待
'''
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import presence_of_element_located, visibility_of, \
    element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait

from config.config_1 import file,url,driver_file
from selenium.webdriver.support.select import Select



s = Service(driver_file)
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(10)
driver.get(url)
driver.maximize_window()


driver.find_element(By.ID, "account").send_keys("shelly")
driver.find_element(By.NAME, "password").send_keys("p@ssw0rd")
driver.find_element(By.ID, "submit").click()

driver.find_element(By.LINK_TEXT,"组织").click()
driver.find_element(By.LINK_TEXT,"添加用户").click()

driver.find_element(By.ID, "account").send_keys("shelly11")
driver.find_element(By.NAME, "password1").send_keys("p@ssw0rd")
driver.find_element(By.NAME, "password2").send_keys("p@ssw0rd")
driver.find_element(By.ID, "realname").send_keys("shelly11")
# 下拉框
select_element = driver.find_element(By.ID,"role")
Select(select_element).select_by_visible_text("测试主管")
# Select(select_element).select_by_value("qd")
# Select(select_element).select_by_index(7)

driver.find_element(By.NAME,"verifyPassword").send_keys("p@ssw0rd")

# 利用javascript脚本写滚动条
js = "document.documentElement.scrollTop = 1000"
driver.execute_script(js)

driver.find_element(By.ID,"submit").click()


driver.find_element(By.LINK_TEXT,"用户").click()
driver.find_element(By.ID,"bysearchTab").click()
driver.find_element(By.ID,"value1").send_keys("shelly11")
driver.find_element(By.ID,"submit").click()

time.sleep(1)
driver.find_element(By.CLASS_NAME,"icon-trash").click()


# 切换页面框
driver.switch_to.frame("iframe-triggerModal")
driver.find_element(By.NAME,"verifyPassword").send_keys("p@ssw0rd")
driver.find_element(By.ID,"submit").click()

# 切换回原来得页面框
driver.switch_to.default_content()
driver.find_element(By.ID,"submit").click()
