'''
@File:Pagelogin.py
@DateTime:17/12/2021 下午 9:01
@Author:sweet
@Desc:
'''
from selenium.webdriver.common.by import By


class Loginpage:
    def __init__(self,driver):
        self.driver = driver
        self.account = By.ID,"account"
        self.password = By.NAME,"password"
        self.button_login = By.ID,"submit"
        self.button_user = By.CLASS_NAME,"user-name"
        self.button_logout = By.LINK_TEXT,"退出"

    def type_username(self,username):
        self.driver.find_element(*self.account).send_keys(username)

    def type_password(self,password):
        self.driver.find_element(*self.password).send_keys(password)

    def cilck_login(self):
        self.driver.find_element(*self.button_login).click()

    def click_logout(self):
        self.driver.find_element(*self.button_user).click()
        self.driver.find_element(*self.button_logout).click()