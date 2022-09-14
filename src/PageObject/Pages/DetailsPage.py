import time

from src.imports import *

class DetailsPage:
    def __init__(self, driver):
        self.driver             = driver
        self.editBtn            = '//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[1]/div/a/button'
        self.detPageBody        = '//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div/div'
        self.locationBtn        = '//*[@id="simple-tab-0"]'
        self.geofenceBtn        = '//*[@id="simple-tab-1"]'
        self.truckPathsBtn      = '//*[@id="simple-tab-2"]'
        self.visitTrendsBtn     = '//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[1]'
        self.lastMonthBtn       = '//*[@id="root"]/div/div/div[1]/div/div/div/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/div[2]/div[2]'
        self.scrollDownPage     = 'window.scrollTo(0,document.body.scrollHeight)'
        self.scrollTopPage      = 'window.scrollTo(0,0)'

    def get_element_tab(self):
        return self.driver.window_handles

    def get_element_editDetails_btn(self):
        return self.driver.find_element(By.XPATH, self.editBtn)

    def get_element_location_btn(self):
        return self.driver.find_element(By.XPATH, self.locationBtn)

    def get_element_geofence_btn(self):
        return self.driver.find_element(By.XPATH, self.geofenceBtn)

    def get_element_trucks_paths_btn(self):
        return self.driver.find_element(By.XPATH, self.truckPathsBtn)

    def get_element_visitTrends_btn(self):
        return self.driver.find_element(By.XPATH, self.visitTrends)

    def get_element_lastMonthBtn_btn(self):
        return self.driver.find_element(By.XPATH, self.lastMonthBtn)

    def get_action_scroll_down(self):
        return self.driver.execute_script(self.scrollDownPage)

    def get_action_scroll_top(self):
        return self.driver.execute_script(self.scrollTopPage)

    def switching_tabs(self):
        for handle in self.get_element_tab():
            self.driver.switch_to.window(handle)
            print(self.driver)

    def current_tab(self):
        self.switching_tabs()
        # print('Estos son los IDs de las pestañas abiertas:   ', handles)
        # print('Current Tab Flag')
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.detPageBody))
                # Edit Details button
            )

        finally:
            pass
            # self.get_element_geofence_btn().click()
            # time.sleep(2)
            # self.get_element_trucks_paths_btn().click()
            # time.sleep(2)
            # self.get_action_scroll_down()
            # time.sleep(5)
            # self.get_action_scroll_top()
            # time.sleep(5)
            # self.get_element_editDetails_btn().click()

        # time.sleep(5)
            # time.sleep(5)
            # time.sleep(15)
            # driver.close()

########## Location, Geofence & Truck Paths ################
############################################################

    def location_geofence_truck(self):
        self.current_tab()
        self.get_element_location_btn().click()
        time.sleep(2)
        self.get_element_geofence_btn().click()
        time.sleep(2)
        self.get_element_trucks_paths_btn().click()
        time.sleep(2)
        self.get_element_editDetails_btn().click()

########## Analytics Section (Loca details page) ################
#################################################################
    def analytics(self):
        self.current_tab()
        self.get_action_scroll_down()
        time.sleep(5)
        self.get_element_lastMonthBtn_btn().click()
        time.sleep(5)
        self.get_action_scroll_top()
        self.get_element_editDetails_btn().click()

