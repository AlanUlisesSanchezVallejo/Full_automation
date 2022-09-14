import random

from src.imports import *
from src.PageObject.Pages.EditDetailsPage import *

class LocationName:
    def __init__(self, driver):
        self.driver             = driver
        self.mainName           = '//*[@id="locationMainName"]'

    def get_element_main_name(self):
        return self.driver.find_element(By.XPATH, self.mainName)

    def get_random_name(self):
        return str(random.randint(0, 100))


    def update_main_name(self, name, file):
            self.get_element_main_name().send_keys(Keys.CONTROL+"A")
            self.get_element_main_name().send_keys(Keys.DELETE)
            rand = str(random.randint(0, 100))
            self.get_element_main_name().send_keys(name, rand)
            file.write('Location Name: ' + name + rand + os.linesep)
            time.sleep(5)

