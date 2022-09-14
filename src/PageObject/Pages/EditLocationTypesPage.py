from src.imports import *

class LocationTypes:
    def __init__(self, driver):
        self.driver         = driver
        self.type           = ''
        self.rand = str(random.randint(1, 6))

    def get_element_random_type(self):

        self.type   = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div/div/p['+self.rand+']/label'
        return self.driver.find_element (By.XPATH, self.type)

    def update_location_type(self, file):
        file.write('Location Type selected: ' + self.rand + os.linesep)
        self.get_element_random_type().click()
        time.sleep(5)

