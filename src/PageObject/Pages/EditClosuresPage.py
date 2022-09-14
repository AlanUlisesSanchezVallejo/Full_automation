import random

from src.imports import *

class Closures:
    def __init__(self, driver):
        self.driver             = driver
        # self.toogle

    def get_random_closure(self):
        return random.randint(0, 1)

    def update_closures(self, file):
        file.write('--- Closures ----' + os.linesep)
        for i in [3, 4, 5, 6, 7, 8]:
            if (self.get_random_closure() == 1):
                toogle = self.driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[' + str(i) + ']/div')
                toogle.click()
                file.write('   Toogle ' + str(i-2) + ': Click' + os.linesep)

            elif (self.get_random_closure() == 0):
                continue

        time.sleep(5)






