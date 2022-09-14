from src.imports import *

class MyCompany:
    def __init__(self, driver): # getting XPATH or component IDs
        self.driver                     = driver
        self.myCompanyBtn               = '//*[@id="root"]/div/div/div[1]/nav/div/div[1]/a[2]'
        self.myCompanyBody              = '//*[@id="root"]/div/div/div[1]/div/div[2]/div[2]'

    def get_element_myCompany_btn(self):
        return self.driver.find_element(By.XPATH, self.myCompanyBtn)

    def get_element_myCompanyBody(self):
        return self.driver.find_element(By.XPATH, self.myCompanyBody)

    def myCompany(self):
        self.get_element_myCompany_btn().click()
        try:
            element = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located((By.XPATH, self.myCompanyBody))
            )

        except:
            print('My company Page was not displayed')

        finally:
            time.sleep(5)

