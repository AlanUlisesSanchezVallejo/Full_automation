from src.imports import *

class NewUserRequest:
    def __init__(self, driver):
        self.driver                         = driver
        self.userType                       = '//*[@id="externalUserTypeId"]'
        self.firstName                      = '//*[@id="firstName"]'
        self.lastName                       = '//*[@id="lastName"]'
        self.jobTitle                       = '//*[@id="title"]'
        self.email                          = '//*[@id="email"]'
        self.phone                          = '//*[@id="phoneNumber"]'
        self.companyName                    = '//*[@id="companyName"]'
        self.companyWebsite                 = '//*[@id="companyWebsite"]'
        self.city                           = '//*[@id="companyCity"]'
        self.state                          = '//*[@id="companyStateCode"]'

    def get_element_user_type(self):
        return self.driver.find_element(By.XPATH, self.userType)

    def get_element_first_name(self):
        return self.driver.find_element(By.XPATH, self.firstName)

    def get_element_last_name(self):
        return self.driver.find_element(By.XPATH, self.lastName)

    def get_element_job_title(self):
        return self.driver.find_element(By.XPATH, self.jobTitle)

    def get_element_email(self):
        return self.driver.find_element(By.XPATH, self.email)

    def get_element_phone(self):
        return self.driver.find_element(By.XPATH, self.phone)

    def get_element_company_name(self):
        return self.driver.find_element(By.XPATH, self.companyName)

    def get_element_company_name(self):
        return self.driver.find_element(By.XPATH, self.companyName)

    def get_element_company_website(self):
        return self.driver.find_element(By.XPATH, self.companyWebsite)

    def get_element_city(self):
        return self.driver.find_element(By.XPATH, self.city)

    def get_element_state(self):
        return self.driver.find_element(By.XPATH, self.state)

    def new_user_request(self, first_name, last_name, job_title, email, phone, companyName, companyWebsite, city, state):
        self.get_element_company_name().send_keys(first_name)
        self.get_element_last_name().send_keys(last_name)
        self.get_element_job_title().send_keys(job_title)
        self.get_element_email().send_keys(email)
        self.get_element_phone().send_keys(phone)
        self.get_element_company_name().send_keys(companyName)
        self.get_element_company_website().send_keys(companyWebsite)
        self.get_element_city().send_keys(city)
        self.get_element_state().send_keys(state)


