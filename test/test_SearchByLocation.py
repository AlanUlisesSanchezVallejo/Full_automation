import time
import unittest

import HtmlTestRunner

from src.PageObject.Pages import SearchByLocation
from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *


class Test_SearchByLocation(WebDriverSetup):
    def test_searchByLocation(self):
        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        time.sleep(3)

        searchpage = SearchByLocation(driver)
        searchpage.search('Solera', 'Roanoke', 'Texas')
        time.sleep(10)



if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C'))
