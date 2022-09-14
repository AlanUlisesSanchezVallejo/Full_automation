from src.imports import *

class Amenities:
    def __init__(self, driver):
        self.driver                             = driver
        self.additionalAmenitiesTextbox         = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div/div[1]/div/input[1]'
        self.additionalAmenitiesAddBtn          = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div[1]/div[2]'
        self.newSelection                       = '//*[@id="additional-amenity0-item-0"]'

    def get_element_additional_Amenities_Txt(self):
        return self.driver.find_element(By.XPATH, self.additionalAmenitiesTextbox)

    def get_element_addtional_Amenities_Btn(self):
        return self.driver.find_element(By.XPATH, self.additionalAmenitiesAddBtn)

    def get_element_new_selection_box(self):
        return self.driver.find_element(By.XPATH, self.newSelection)

    def update_amenities(self, file):
        file.write('--- Amenities ---' + os.linesep)
        for i in [1, 2, 3, 4, 5, 6]:
                rand = random.randint(1, 2)
                radioBtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[' + str(i) + ']/div[3]/p[' + str(rand) + ']/label')
                radioBtn.click()
                file.write('    Amenitie ' + str(i) + ': ' + str(rand) + os.linesep)
                # time.sleep


    #### Adding random Additional Amenities ########
    ################################################

    def update_additional_amenities(self, file):

        additionalAmenities = ['Additional ' + str(random.randint(1, 1000)),
                               'Additional ' + str(random.randint(1, 1000)),
                               'Additional ' + str(random.randint(1, 1000))]  # These are just examples
        i = 0
        # amenityTXT = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div/div[1]/div/input[1]')
        # addBtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div[1]/div[2]')

        while i < len(additionalAmenities):
            self.get_element_additional_Amenities_Txt().send_keys(additionalAmenities[i])
            time.sleep(2)
            # newSelection = self.driver.find_element(By.XPATH, '//*[@id="additional-amenity0-item-0"]')  # New selection box when user inserts a value
            self.get_element_new_selection_box().click()
            self.get_element_addtional_Amenities_Btn().click()
            file.write('    Additional Amenitie added: ' + additionalAmenities[i] + os.linesep)
            time.sleep(2)
            i += 1

        ##### Deleting a random Additional Amenitie ########
        ####################################################

        deleteRand = random.randint(2, len(additionalAmenities) + 1)

        delete = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[3]/form/div/div[' + str(deleteRand) + ']/div[2]')
        delete.click()
        file.write('    Additional Amenitie DELETED: ' + str(deleteRand) + os.linesep)

    time.sleep(5)



