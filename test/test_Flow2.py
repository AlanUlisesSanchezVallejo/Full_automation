import time
import unittest

from src.imports import *
from src.PageObject.Pages import SearchByLocation
from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *
# from test.test_SearchByLocation import *
from src.PageObject.Pages.EditDetailsPage import *
from src.PageObject.Pages.MyCompanyPage import *
from src.PageObject.Pages.InternalAdminPortal import *
from src.PageObject.Pages.Logout import *


class Test_Flow2(WebDriverSetup):
    def test_Regression_test_2(self):
        # self.file = open(r'C:\Users\Alan Sanchez\Desktop\FLow1_Automation\Flow2.txt', 'w')
        driver = self.driver
        self.driver.get('http://omnitracslabs.com/login')
        home_page = HomePage(driver)
        home_page.new_user_request('Regression', 'Test', 'QA', 'Regression_testing' + str(random.randint(1, 100)) + '@mail.com', '0123456789', 'Omnitracs',
                                   'omnitracs.com', 'San Francisco', 'CA')
        time.sleep(8)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        # home_page.login('Kjohnstone@omnitracs.com', 'Omni123')  #For PROD
        time.sleep(3)

        searchAddress = SearchByLocation(driver)
        searchAddress.searchByAddress('1500 Solana Blvd Ste 6300 Bldg 6', 'Roanoke', 'Texas')

        time.sleep(2)

        DetailsPage(driver).analytics()

        MyCompany(driver).myCompany() #My Company page

        InternalAdmin(driver).internalAdmin_portal() #Internal Admin Page, it only works with internal users#

        LogOut(driver).logOut()

if __name__ == '__main__':
    unittest.main()
