import os
import time

from src.imports import *

class Services:
    def __init__(self, driver):
        self.driver                     = driver
        self.lumperServiceNO            = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/p[2]/label'
        self.lumperServiceYES           = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/p[1]/label'
        self.lumperFee                  = 'lumperCost'
        self.currency                   = 'currencyType'

    def get_element_lumperService_NO(self):
        return self.driver.find_element(By.XPATH, self.lumperServiceNO)

    def get_element_lumperServiceYes(self):
        return self.driver.find_element(By.XPATH, self.lumperServiceYES)

    def get_element_lumper_FEE(self):
        return self.driver.find_element(By.ID, self.lumperFee)

    def get_element_currency_type(self):
        return self.driver.find_element(By.ID, self.currency)

    def update_services(self, file):
        file.write('--- SERVICES ---' + os.linesep)
        rand = random.randint(0, 1)

        ######## Lumper Service (YES/NO) ######
        if (rand == 0):
            self.get_element_lumperService_NO().click()
            file.write('    NO Lumper Service' + os.linesep)

        else:
            self.get_element_lumperServiceYes().click()

            dolarRand = random.randint(0, 9999)
            centsRand = random.randint(0, 99)
            self.get_element_lumper_FEE().send_keys(str(dolarRand) + '.' + str(centsRand))

            currency = Select(self.driver.find_element(By.ID, 'currencyType'))
            currencyRand = random.randint(0, 1)
            if (currencyRand == 0):
                currency.select_by_visible_text('USD')
                file.write('    ' + str(dolarRand) + '.' + str(centsRand) + ' USD' + os.linesep)
            else:
                currency.select_by_visible_text('CAD')
                file.write('    ' + str(dolarRand) + '.' + str(centsRand) + ' CAD' + os.linesep)

            ######## Payment Option ############
            for i in [1, 2, 3, 4]:
                paymentOption = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/div[3]/div[' + str(i) + ']/label')
                paymentOptionRand = random.randint(0, 1)

                if (paymentOptionRand == 0):
                    continue
                else:
                    paymentOption.click()
                    file.write('    Required Equipment' + str(i) +': ' + 'Click' + os.linesep)
        time.sleep(5)


