from src.imports import *

class HomePage:
    def __init__(self,  driver):
        self.driver     = driver
        self.user       = 'email'
        self.password   = 'password'
        self.submit     = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/form/button'


    def get_element_user(self):
        return self.driver.find_element('id', self.user)

    def get_element_password(self):
        return self.driver.find_element('id', self.password)

    def get_element_submit(self):
        return self.driver.find_element('xpath', self.submit)

    def login(self, user, password):
        self.get_element_user().send_keys(user)
        self.get_element_password().send_keys(password)
        self.get_element_submit().click()







