import time
import unittest

from src.PageObject.Pages import SearchByLocation
from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *
# from test.test_SearchByLocation import *
from src.PageObject.Pages.EditDetailsPage import *



class Test_LocationType(WebDriverSetup):
    def test_editsLocationType(self):
        self.file = open(r'C:\Users\Alan Sanchez\Desktop\FLow1_Automation\status.txt', 'w')

        driver = self.driver
        self.driver.get('http://dev.omnitracslabs.com')
        home_page = HomePage(driver)
        time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        time.sleep(3)

        searchpage = SearchByLocation(driver)
        searchpage.search('Solera', 'Roanoke', 'Texas')
        time.sleep(2)
        DetailsPage(driver).location_geofence_truck()
        # DetailsPage(driver).analytics()

        EditDetailsPage(driver).edit_location_type(self.file)

        self.file.close()

if __name__ == '__main__':
    unittest.main()