'''
@File:login_out.py
@DateTime:2021/12/10 18:07
@Author:sweet
@Desc:
'''

from selenium.webdriver.common.by import By

class log_in_out:
    def __init__(self,driver):
        self.username = By.ID,"account"
        self.password = By.NAME,"password"
        self.login = By.ID,"submit"
        self.bowser = driver

    def input_username(self,username):
        self.bowser.find_element(*self.username).send_keys(username)

    def input_password(self, password):
        self.bowser.find_element(*self.password).send_keys(password)

    def click_login(self):
        self.bowser.find_element(*self.login).click()
