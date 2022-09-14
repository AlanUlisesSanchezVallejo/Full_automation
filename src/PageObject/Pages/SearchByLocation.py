from Src.imports import *
class SearchByLocation:

    def __init__(self, driver):
        self.driver                     = driver
        self.name                       = 'name'
        self.city                       = 'city'
        self.state                      = 'state'
        self.searchBtn                  = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/form/div[2]/div/button[1]'
        self.searchResults              = 'search-results'
        self.results                    = '//*[@id="root"]/div/div/div[1]/div/div/div[3]/div[1]/div[2]/a[1]/div'

        self.flag                       = False
        self.searchByAddressBtn         = '/html/body/div[1]/div/div/div[1]/div/div/div[1]/form/div[1]/div[1]/label[2]' # or /html/body/div/div/div/div[1]/div/div/div[1]/form/div[1]/div[1]/label[2]
        self.addressTextBox             = 'address'

    def get_element_name(self):
        return self.driver.find_element(By.ID, self.name)

    def get_element_city(self):
        return self.driver.find_element(By.ID, self.city)

    def get_element_state(self):
        return self.driver.find_element(By.ID, self.state)

    def get_element_search_button(self):
        return self.driver.find_element(By.XPATH, self.searchBtn)

    def element_search_result_btn(self):
        return self.driver.find_element(By.XPATH, self.results)

    def get_element_searchByAddress_btn(self):
        return self.driver.find_element(By.XPATH, self.searchByAddressBtn)

    def get_element_address(self):
        return self.driver.find_element(By.ID, self.addressTextBox)





    def search(self, name, city, state):
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.ID, self.name))
            )
        finally:
            if (self.flag):
                self.get_element_address().send_keys(name)
            else:
                self.get_element_name().send_keys(name)
            self.get_element_city().send_keys(city)
            #self.get_element_state().select_by_visible_text(state)
            self.get_element_state().send_keys(state)
            self.get_element_search_button().click()

        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.CLASS_NAME, self.searchResults))
            )
        finally:
            # selectResult = driver.find_element("xpath", "//*[@id='root']/div/div/div[1]/div/div/div[3]/div[1]/div[2]/a[1]/div")
            self.element_search_result_btn().click()
            # time.sleep(3)

    def searchByAddress(self, address, city, state):
        self.get_element_searchByAddress_btn().click()
        self.flag = True
        self.search(address, city, state)






















