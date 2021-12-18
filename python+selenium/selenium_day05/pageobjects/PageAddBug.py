'''
@File:PageAddBug.py
@DateTime:18/12/2021 下午 1:47
@Author:sweet
@Desc:
'''

from selenium.webdriver.common.by import By

class AddBugPage:
    def __init__(self,driver):
        self.driver = driver
        self.account = By.ID,"account"
        self.password = By.NAME,"password"
        self.buttonlogin = By.ID,"submit"

    def type_username(self,username):
        self.driver.find_element(*self.account).send_keys(username)

    def type_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.buttonlogin).click()