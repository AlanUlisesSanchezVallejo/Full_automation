from src.imports import *

class AppointmentScheduling:
    def __init__(self, driver):
        self.driver                     = driver
        self.appointmentType            = '//*[@id="appointmentType"]'
        self.specialInstructions        = '//*[@id="specialInstructions"]'
        self.online                     = '//*[@id="websiteAddress"]'
        self.byPhone                    = '//*[@id="phoneNumber"]'
        self.byEmail                    = '//*[@id="emailAddress"]'
        self.error                      = 'bh-error'

    def get_element_appointment_type(self):
        return self.driver.find_element(By.XPATH, self.appointmentType)

    def get_element_special_instructions(self):
        return self.driver.find_element(By.XPATH, self.specialInstructions)

    def get_element_online(self):
        return self.driver.find_element(By.XPATH, self.online)

    def get_element_byPhone(self):
        return self.driver.find_element(By.XPATH, self.byPhone)

    def get_element_byEmail(self):
        return self.driver.find_element(By.XPATH, self.byEmail)

    def get_element_error(self):
        return self.driver.find_element(By.CLASS_NAME, self.error)


    def update_appointment(self, online_page, email, email_domain, file):
        file.write('--- Appointment Scheduling ---' + os.linesep)
        state = Select(self.driver.find_element('xpath', '//*[@id="appointmentType"]'))  # Scroll Down menu appointment Type
        rand = random.randint(0, 1)

        if (rand == 0):
            state.select_by_visible_text('FCFS')
            file.write('    FCFS was selected' + os.linesep)

        else:
            state.select_by_visible_text('By Appointment Only')
            file.write('    By Appointment Only was selected' + os.linesep)

            # Fill ONLINE, BY Phone and  By email fields
            for i in [1, 2, 3]:
                randomClick = random.randint(0, 1)  # Click or not the checkboxes randomly
                onlineBtn = self.driver.find_element('xpath', '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div[' + str(i) + ']/label/span')
                if randomClick == 0:
                    continue
                else:
                    onlineBtn.click()
                    try:
                        self.get_element_error()
                        #error = self.driver.find_element(By.CLASS_NAME, 'bh-error')  # Error class whe textbox is open and there is not any value (webpage, phone or email)
                    except:
                        print('except')
                    else:
                        if (i == 1):
                            self.get_element_online().send_keys(online_page)
                            file.write('        Online: ' + online_page + os.linesep)

                        elif (i == 2):
                            randPhone = random.randint(1000000000, 9999999999)
                            self.get_element_byPhone().send_keys(randPhone)
                            file.write('        Phone: ' + str(randPhone) + os.linesep)

                        elif (i == 3):
                            randEmail = random.randint(0, 100)
                            self.get_element_byEmail().send_keys(email + str(randEmail) + email_domain)
                            file.write('        Email: ' + email + str(randEmail) + email_domain + os.linesep)

    def update_special_instructions(self, special_instructions, file):

        self.get_element_special_instructions().send_keys(Keys.CONTROL, "A")
        self.get_element_special_instructions().send_keys(Keys.DELETE) # Delete all existing text on this box
        self.get_element_special_instructions().send_keys(special_instructions)
        file.write('        Special instructions: ' + special_instructions + os.linesep)

        time.sleep(5)