import time

from src.PageObject.Pages import HomePage
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import HomePage

class Test_Login(WebDriverSetup):
    def test_login(self):
        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        # time.sleep(1)
        home_page.new_user_request('Alan', 'Sanchez', 'QA', 'alan_QA@mail.com', '0123456789', 'Omnitracs', 'omnitracs.com', 'San Francisco', 'CA')
        time.sleep(10)


