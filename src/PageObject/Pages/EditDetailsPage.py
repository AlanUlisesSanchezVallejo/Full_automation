import time

from src.imports import *
from src.PageObject.Pages.EditLocationNamePage import LocationName
from src.PageObject.Pages.EditLocationTypesPage import LocationTypes
from src.PageObject.Pages.EditContactsPage import EditContacts
from src.PageObject.Pages.EditBusinessHoursPage import BusinessHours
from src.PageObject.Pages.EditClosuresPage import Closures
from src.PageObject.Pages.EditAppointmentSchedulingPage import AppointmentScheduling
from src.PageObject.Pages.EditAmenitiesPage import Amenities
from src.PageObject.Pages.EditServicesPage import Services
from src.PageObject.Pages.EditSafetyRequirementsPage import SafetyRequirements
from src.PageObject.Pages.EditProceduresPage import Procedures


class EditDetailsPage:
    def __init__(self, driver): # getting XPATH or component IDs
        self.driver                         = driver
        self.cancelBtn                      = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div[2]/button[1]'
        self.submitBtn                      = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div[2]/button[2]'
        self.locationNameBtn                = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[1]'
        self.locationTypeBtn                = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[3]'
        self.contactsBtn                    = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[4]'
        self.businessHoursBtn               = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[5]'
        self.closuresBtn                    = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[6]'
        self.appointmentSchedulingBtn       = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[7]'
        self.amenitiesBtn                   = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[8]'
        self.servicesBtn                    = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[9]'
        self.safetyRequirementsBtn          = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[10]'
        self.proceduresBtn                  = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div[2]/div[1]/div[11]'


    def get_element_cancel_btn(self): #getting the components inside the edits page
        return self.driver.find_element(By.XPATH, self.cancelBtn)

    def get_element_submit_btn(self):
        return self.driver.find_element(By.XPATH, self.submitBtn)

    def get_element_location_name_btn(self):
        return self.driver.find_element(By.XPATH, self.locationNameBtn)

    def get_element_location_type_btn(self):
        return self.driver.find_element(By.XPATH, self.locationTypeBtn)

    def get_element_contacts_btn(self):
        return self.driver.find_element(By.XPATH, self.contactsBtn)

    def get_element_business_hours_btn(self):
        return self.driver.find_element(By.XPATH, self.businessHoursBtn)

    def get_element_closures_btn(self):
        return self.driver.find_element(By.XPATH, self.closuresBtn)

    def get_element_appointment_scheduling_btn(self):
        return self.driver.find_element(By.XPATH, self.appointmentSchedulingBtn)

    def get_element_amenities_btn(self):
        return self.driver.find_element(By.XPATH, self.amenitiesBtn)

    def get_element_services_btn(self):
        return self.driver.find_element(By.XPATH, self.servicesBtn)

    def get_element_safety_requirements_btn(self):
        return self.driver.find_element(By.XPATH, self.safetyRequirementsBtn)

    def get_element_procedures_btn(self):
        return self.driver.find_element(By.XPATH, self.proceduresBtn)

    def click_cancel_btn(self):
        self.get_element_cancel_btn().click()

    def click_submit_btn(self):
        self.get_element_submit_btn().click()
        time.sleep(10)

    def edit_location_name(self, name, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.locationNameBtn))
            )
        finally:
            self.get_element_location_name_btn().click()
            locationName = LocationName(self.driver)
            locationName.update_main_name(name, file)

    def edit_location_type(self, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.locationTypeBtn))
            )
        finally:
            self.get_element_location_type_btn().click()
            locationType = LocationTypes(self.driver)
            locationType.update_location_type(file)

    def edit_contacts(self, email, email_domain, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.contactsBtn))
            )
        finally:
            self.get_element_contacts_btn().click()
            contacts = EditContacts(self.driver)
            contacts.update_contacts(email, email_domain, file)

    def edit_business_hours(self, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.businessHoursBtn))
            )
        finally:
            self.get_element_business_hours_btn().click()
            businessHours = BusinessHours(self.driver)
            businessHours.update_business_hours(file)

    def edit_closures(self, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.closuresBtn))
            )
        finally:
            self.get_element_closures_btn().click()
            closures = Closures(self.driver)
            closures.update_closures(file)

    def edit_appointment_scheduling(self, online_page, email, email_domain, special_instructions, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.appointmentSchedulingBtn))
            )
        finally:
            self.get_element_appointment_scheduling_btn().click()
            appointmentScheduling = AppointmentScheduling(self.driver)
            appointmentScheduling.update_appointment(online_page, email, email_domain, file)
            appointmentScheduling.update_special_instructions(special_instructions, file)

    def edit_amenities(self, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.amenitiesBtn))
            )
        finally:
            self.get_element_amenities_btn().click()
            amenities = Amenities(self.driver)
            amenities.update_amenities(file)
            amenities.update_additional_amenities(file)

    def edit_services(self, file):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.servicesBtn))
            )
        finally:
            self.get_element_services_btn().click()
            services = Services(self.driver)
            services.update_services(file)

    def edit_safety_requirements(self, file, covid_protocols_text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.safetyRequirementsBtn))
            )
        finally:
            self.get_element_safety_requirements_btn().click()
            safetyRequirements = SafetyRequirements(self.driver)
            safetyRequirements.update_safetyRequirements(file)
            safetyRequirements.update_additionalSafetyRequirements(file)
            safetyRequirements.update_covid_protocols(file, covid_protocols_text)
            safetyRequirements.update_pets_allowed(file)

    def edit_procedures(self, file, additional_driver_text):
        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.proceduresBtn))
            )
        finally:
            self.get_element_procedures_btn().click()
            procedures = Procedures(self.driver)
            procedures.update_procedures(file)
            procedures.update_additional_driver_directions(file, additional_driver_text)





