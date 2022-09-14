import time
import unittest

from src.PageObject.Pages import SearchByLocation
from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *
# from test.test_SearchByLocation import *
from src.PageObject.Pages.EditDetailsPage import *


class Test_SearchByAddress(WebDriverSetup):
    def test_seachByAddress(self):
        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        time.sleep(3)

        searchpage = SearchByLocation(driver)
        searchpage.searchByAddress('1500 Solana Blvd Ste 6300 Bldg 6', 'Roanoke', 'Texas')
        time.sleep(3)


if __name__ == '__main__':
    unittest.main()