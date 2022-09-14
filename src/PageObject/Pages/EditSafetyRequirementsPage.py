import time

from src.imports import *

class SafetyRequirements:
    def __init__(self, driver):
        self.driver                     = driver
        self.addEquipmentTXT            = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div[1]/div[1]/div/input[1]'
        self.addEquipmentBtn            = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div[1]/div[2]'
        self.newSelectionBox            = '//*[@id="additional-equipment0-item-0"]' # New selection box when user inserts a value
        self.covidProtocols             = 'covidProtocolInstructions'


    def get_element_add_Equipment_textbox(self):
        return self.driver.find_element(By.XPATH, self.addEquipmentTXT)

    def get_element_add_Equipment_Btn(self):
        return self.driver.find_element(By.XPATH, self.addEquipmentBtn)

    def get_element_new_Selection_box(self):
        return self.driver.find_element(By.XPATH, self.newSelectionBox)

    def get_element_covid_protocols(self):
        return self.driver.find_element(By.ID, self.covidProtocols)

    def update_safetyRequirements(self, file):
        file.write('--- Safety Requirements ---' + os.linesep)
        for i in [1, 2, 3, 4, 5]:
            requiredEquipment = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[1]/div[3]/div[' + str(i) + ']/label')
            requiredRand = random.randint(0, 1)
            if (requiredRand == 0):
                continue
            else:
                requiredEquipment.click()
                file.write('    Safety Req ' +str(i) + ' Click' + os.linesep)


    ################## Updating Additional Safety Requirements #################
    ############################################################################

    def update_additionalSafetyRequirements(self, file):
        additionalSafetyReq = ['Additional testing ' + str(random.randint(1, 1000)),
                               'Additional testing ' + str(random.randint(1, 1000)),
                               'Additional testing ' + str(random.randint(1, 1000))]

        i = 0

        while i < len(additionalSafetyReq):
            self.get_element_add_Equipment_textbox().send_keys(additionalSafetyReq[i])
            time.sleep(2)
            self.get_element_new_Selection_box().click()
            self.get_element_add_Equipment_Btn().click()
            file.write('    Additional Safety Requirement added: ' + additionalSafetyReq[i] + os.linesep)

            time.sleep(1)
            i += 1


        ################## deleting a random Additional Safety Requirement #######################
        deleteRand = random.randint(2, len(additionalSafetyReq) + 1)

        delete = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/form/div/div[' + str(deleteRand) + ']/div[2]')
        delete.click()

        ############################################################################
        ############################################################################



    def update_covid_protocols(self, file, covid_protocols_text):
        ################## COVID PROTOCOLS ##################
        self.get_element_covid_protocols().send_keys(Keys.CONTROL + "A")
        self.get_element_covid_protocols().send_keys(Keys.DELETE)
        self.get_element_covid_protocols().send_keys(covid_protocols_text)
        file.write('    Covid Protocols: ' + covid_protocols_text + os.linesep)

    def update_pets_allowed(self, file):
        ################## Pets allowed ##################
        petRand = random.randint(1, 2)
        petsAllowed = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[4]/div[3]/p[' + str(petRand) + ']/label')
        petsAllowed.click()
        file.write('    Pets Allowed: ' + str(petRand) + os.linesep)


        time.sleep(5)

