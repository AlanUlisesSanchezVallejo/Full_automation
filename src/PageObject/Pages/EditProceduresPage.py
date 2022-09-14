from src.imports import *

class Procedures:
    def __init__(self, driver):
        self.driver                 = driver
        self.additionalDriver       = 'drivingDirections'

    def get_element_additional_driver_directions(self):
        return self.driver.find_element(By.ID, self.additionalDriver)

    def update_procedures(self, file):
        file.write('--- Procedures ---' + os.linesep)
        for i in [1, 2, 3]:
            radioBtnRand = random.randint(1, 2)
            radioBtn = self.driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[' + str(i) + ']/div[3]/p[' + str(radioBtnRand) + ']/label')
            radioBtn.click()
            file.write('    Procedure ' + str(i) + ': ' + str(radioBtnRand) + os.linesep)

    def update_additional_driver_directions(self, file, additional_driver_text):
        self.get_element_additional_driver_directions().send_keys(Keys.CONTROL, "A")
        self.get_element_additional_driver_directions().send_keys(Keys.DELETE)
        self.get_element_additional_driver_directions().send_keys(additional_driver_text)
        file.write ('    Additional directions: ' + additional_driver_text + os.linesep)

        time.sleep(5)