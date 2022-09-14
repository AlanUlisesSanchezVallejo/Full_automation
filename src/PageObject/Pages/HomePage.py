from src.imports import *

class HomePage:
    def __init__(self,  driver):
        self.driver     = driver
        self.user       = 'email'
        self.password   = 'password'
        self.submit     = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/form/button'

        ################## NEW USER REQUEST ELEMENTS ###############################
        self.notAMember             = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/div/button'
        self.userType               = '//*[@id="externalUserTypeId"]'
        self.firstName              = '//*[@id="firstName"]'
        self.lastName               = '//*[@id="lastName"]'
        self.jobTitle               = '//*[@id="title"]'
        self.newEmail               = '/html/body/div[3]/div/div/div[2]/form/div[4]/div[1]/div/input'
        self.phone                  = '//*[@id="phoneNumber"]'
        self.companyName            = '//*[@id="companyName"]'
        self.companyWebsite         = '//*[@id="companyWebsite"]'
        self.city                   = '//*[@id="companyCity"]'
        self.state                  = '//*[@id="companyStateCode"]'
        self.saveBtn                = '/html/body/div[3]/div/div/div[3]/button[2]'
        self.cancelBtn              = '/html/body/div[3]/div/div/div[3]/button[1]'
        ##############################################################################

    def get_element_user(self):
        return self.driver.find_element('id', self.user)

    def get_element_password(self):
        return self.driver.find_element('id', self.password)

    def get_element_submit(self):
        return self.driver.find_element('xpath', self.submit)

    ##################### NEW USER REQUEST ###############################
    def get_element_not_a_member(self):
        return self.driver.find_element(By.XPATH, self.notAMember)

    def get_element_user_type(self):
        return self.driver.find_element(By.XPATH, self.userType)

    def get_element_first_name(self):
        return self.driver.find_element(By.XPATH, self.firstName)

    def get_element_last_name(self):
        return self.driver.find_element(By.XPATH, self.lastName)

    def get_element_job_title(self):
        return self.driver.find_element(By.XPATH, self.jobTitle)

    def get_element_email(self):
        return self.driver.find_element(By.XPATH, self.newEmail)

    def get_element_phone(self):
        return self.driver.find_element(By.XPATH, self.phone)

    def get_element_company_name(self):
        return self.driver.find_element(By.XPATH, self.companyName)

    def get_element_company_website(self):
        return self.driver.find_element(By.XPATH, self.companyWebsite)

    def get_element_city(self):
        return self.driver.find_element(By.XPATH, self.city)

    def get_element_state(self):
        return self.driver.find_element(By.XPATH, self.state)

    def get_element_save_btn(self):
        return self.driver.find_element(By.XPATH, self.saveBtn)

    def get_element_cancelbtn(self):
        return self.driver.find_element(By.XPATH, self.cancelBtn)

    ##############################################################################

    def login(self, user, password):
        self.get_element_user().send_keys(user)
        self.get_element_password().send_keys(password)
        self.get_element_submit().click()

    ################## NEW USER REQUEST ELEMENTS ###############################

    def new_user_request(self, first_name, last_name, job_title, email, phone, companyName, companyWebsite, city, state):
        self.get_element_not_a_member().click()


        user_type           = [ "Shipper/Receiver",
                                "Carrier/Driver",
                                "Broker",
                                "Corporate",
                                "3rd Party"]
        randUserType        = random.randint(0, len(user_type)-1)
        self.get_element_user_type().click()
        time.sleep(0.5)
        self.get_element_user_type().send_keys(user_type[randUserType])
        self.get_element_first_name().send_keys(first_name)
        self.get_element_last_name().send_keys(last_name)
        self.get_element_job_title().send_keys(job_title)
        self.get_element_email().send_keys(email)
        self.get_element_phone().send_keys(phone)
        self.get_element_company_name().send_keys(companyName)
        self.get_element_company_website().send_keys(companyWebsite)
        self.get_element_city().send_keys(city)


        state_names     = ["Alaska", "Alabama", "Arkansas", "American Samoa", "Arizona", "California", "Colorado",
                           "Connecticut", "District ", "of Columbia", "Delaware", "Florida", "Georgia", "Guam", "Hawaii",
                           "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts",
                           "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana",
                           "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico",
                           "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Puerto Rico",
                           "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia",
                           "Virgin Islands", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

        rand = random.randint(0, len(state_names)-1)

        self.get_element_state().send_keys(state_names[rand])

        time.sleep(2)

        self.get_element_save_btn().click()

    ##############################################################################


