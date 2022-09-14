import time
from src.imports import *
from src.PageObject.Pages import SearchByLocation
from src.PageObject.Pages.SearchByLocation import SearchByLocation
from src.TestBase.WebDriverSetup import WebDriverSetup
from src.PageObject.Pages.HomePage import *
from src.PageObject.Pages.DetailsPage import *
# from test.test_SearchByLocation import *
from src.PageObject.Pages.EditDetailsPage import *
from src.PageObject.Pages.Logout import *
import HtmlTestRunner
import unittest


class Test_Flow1(WebDriverSetup):

    def test_Regression_test_1(self):
        self.file = open(r'C:\Users\Alan Sanchez\Desktop\FLow1_Automation\status.txt', 'w') # create status.txt file
        driver = self.driver
        self.driver.get('http://omnitracslabs.com/login')
        home_page = HomePage(driver)
        time.sleep(1)
        home_page.login('alanQA@omnitracs.com', 'Omni123+')
        # home_page.login('Kjohnstone@omnitracs.com', 'Omni123')  #For PROD
        time.sleep(3)

        searchpage = SearchByLocation(driver)
        searchpage.search('Solera', 'Roanoke', 'Texas')
        time.sleep(2)
        DetailsPage(driver).location_geofence_truck()
        # DetailsPage(driver).analytics()


        ##All Edit Details page##
        EditDetailsPage(driver).edit_location_name('Solera', self.file)
        EditDetailsPage(driver).edit_location_type(self.file)
        EditDetailsPage(driver).edit_contacts('QA', '@gmail.com', self.file)
        EditDetailsPage(driver).edit_business_hours(self.file)
        EditDetailsPage(driver).edit_closures(self.file)
        EditDetailsPage(driver).edit_appointment_scheduling('www.testing.com', 'alan', '@hotmail.com',
                                                                 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend faucibus risus non pellentesque. '
                                                                 'Nunc interdum condimentum tellus, non sollicitudin erat porta ut. Curabitur imperdiet odio nulla, in euismod '
                                                                 'felis vulputate in. Fusce tempus tempor arcu sit amet auctor. In non tortor at nulla fringilla molestie. Cras nec '
                                                                 'felis quis urna aliquam pellentesque et vehicula eros. Suspendisse scelerisque nec diam eu rhoncus. Suspendisse '
                                                                 'maximus neque neque, sit amet commodo nunc malesuada ut.',
                                                            self.file)
        EditDetailsPage(driver).edit_amenities(self.file)
        EditDetailsPage(driver).edit_services(self.file)
        EditDetailsPage(driver).edit_safety_requirements(self.file, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend faucibus risus non pellentesque. '
                                                 'Nunc interdum condimentum tellus, non sollicitudin erat porta ut. Curabitur imperdiet odio nulla, in '
                                                 'euismod felis vulputate in. Fusce tempus tempor arcu sit amet auctor. In non tortor at nulla fringilla '
                                                 'molestie. Cras nec felis quis urna aliquam pellentesque et vehicula eros. Suspendisse scelerisque nec '
                                                 'diam eu rhoncus. Suspendisse maximus neque neque, sit amet commodo nunc malesuada ut.')
        EditDetailsPage(driver).edit_procedures(self.file, 'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam eleifend faucibus risus non pellentesque. '
                                                'Nunc interdum condimentum tellus, non sollicitudin erat porta ut. Curabitur imperdiet odio nulla, in '
                                                'euismod felis vulputate in. Fusce tempus tempor arcu sit amet auctor. In non tortor at nulla fringilla '
                                                'molestie. Cras nec felis quis urna aliquam pellentesque et vehicula eros. Suspendisse scelerisque nec '
                                                'diam eu rhoncus. Suspendisse maximus neque neque, sit amet commodo nunc malesuada ut.')

        ##Finished with All Edit Details page##

        self.file.close()

        EditDetailsPage(driver).click_submit_btn()
        LogOut(driver).logOut()


if __name__ == '__main__':
    unittest.main()

