import time
import unittest

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage

class Test_Login(WebDriverSetup):
    def test_login(self):
        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        # time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        # time.sleep(3)




if __name__ == '__main__':
    unittest.main()