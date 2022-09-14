from src.imports import *

class LogOut:
    def __init__(self, driver):
        self.driver                             = driver
        self.accountDropDown                    = '//*[@id="account-dropdown"]/a/div'
        self.logOutBtn                          = '//*[@id="account-dropdown"]/div/a[2]'

    def get_element_account_dropDown(self):
        return self.driver.find_element(By.XPATH, self.accountDropDown)

    def get_element_logOutBtn(self):
        return self.driver.find_element(By.XPATH, self.logOutBtn)

    def logOut(self):
        self.get_element_account_dropDown().click()
        self.get_element_logOutBtn().click()
        time.sleep(5)
