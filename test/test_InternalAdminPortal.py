import unittest

from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *
# from test.test_SearchByLocation import *
from src.PageObject.Pages.InternalAdminPortal import *



class Test_InternalAdminPortal(WebDriverSetup):
    def test_internalAdminPortal(self):
        # self.file = open(r'C:\Users\Alan Sanchez\Desktop\FLow1_Automation\Flow2.txt', 'w')
        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        # home_page.login('Kjohnstone@omnitracs.com', 'Omni123')  #For PROD
        time.sleep(10)

        InternalAdmin(driver).internalAdmin_portal()





if __name__ == '__main__':
    unittest.main()
