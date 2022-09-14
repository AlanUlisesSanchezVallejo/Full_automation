import random
import time

from src.imports import *

class EditContacts:
    def __init__(self, driver):
        self.driver         = driver
        self.email          = 'emailAddress'
        self.phone          = 'phone'

    def get_element_email(self):
        return self.driver.find_element(By.ID, self.email)

    def get_element_phone(self):
        return self.driver.find_element(By.ID, self.phone)

    def get_random_email(self):
        return str(random.randint(0, 100))

    def get_random_phone(self):
        return str(random.randint(1111111111, 9999999998))

    def update_contacts(self, email, email_domain, file):
        self.get_element_email().send_keys(Keys.CONTROL+'A')
        self.get_element_email().send_keys(Keys.DELETE)
        randEmail = str(random.randint(0, 100))
        self.get_element_email().send_keys(email + randEmail + email_domain)
        file.write('Location Contact email: ' + email + randEmail + email_domain + os.linesep)

        self.get_element_phone().send_keys(Keys.CONTROL+'A')
        self.get_element_phone().send_keys(Keys.DELETE)
        randPhone = str(random.randint(1111111111, 9999999998))
        self.get_element_phone().send_keys(randPhone)
        file.write('Location Contact phone: ' + randPhone + os.linesep)
        time.sleep(5)


