import random

from src.imports import *
#import random
import string

class InternalAdmin:

    def __init__(self, driver):
        self.driver                     = driver

        self.companyTest                = 'Omnitracs Regression Test'
        self.companyCityTest            = 'Chicago'
        self.companyStateTest           = 'Illinois'
        self.companyWebsiteTest         = 'www.Omnitracs.com'

        self.settingsBtn                = '//*[@id="settings-dropdown"]/a'
        self.internalAdminBtn           = '//*[@id="settings-dropdown"]/div/a'
        self.internalAdminPortalBody    = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div/div[1]'
        self.companiesBtn               = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/div/div[1]/a'
        self.usersBtn                   = '//*[@id="root"]/div/div/div[1]/div/div/div[1]/div/div/div[2]/a'

        self.companyTextBox             = 'name' #ID
        self.cityTextBox                = 'city'
        self.stateSelector              = 'state' #ID
        self.newCompanyBtn              = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/form/button[3]'
        self.searchCompanyBtn           = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div/div[1]/div[1]/form/button[1]'

        self.addCompanyName             = '/html/body/div[3]/div/div/div[2]/form/div[1]/div/input'
        self.addCompanyCity             = '/html/body/div[3]/div/div/div[2]/form/div[2]/div/input'
        self.addCompanyState            = '/html/body/div[3]/div/div/div[2]/form/div[3]/div/select'
        self.addCompanyWebsite          = '/html/body/div[3]/div/div/div[2]/form/div[4]/div/input'
        self.saveNewCompanyBtn          = '/html/body/div[3]/div/div/div[3]/button[2]'

        self.firstNameSearch            = 'firstName' #ID
        self.lastNameSearch             = 'lastName' #ID
        self.companyNameSearch          = 'company' #ID
        self.searchUserBtn              = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/form/button[1]'
        self.newUserBtn                 = '//*[@id="root"]/div/div/div[1]/div/div/div[2]/div/div[2]/div[1]/form/button[3]'

        self.addInternalUserBtn         = '/html/body/div[3]/div/div/div[2]/form/div[1]/label[1]'
        self.firstNameInternalUser      = '/html/body/div[3]/div/div/div[2]/form/div[3]/div/div[1]/div/input'
        self.lastNameInternalUSer       = '/html/body/div[3]/div/div/div[2]/form/div[3]/div/div[2]/div/input'
        self.emailInternalUser          = '/html/body/div[3]/div/div/div[2]/form/div[4]/div[1]/div/input'
        self.passwordInternalUser       = '/html/body/div[3]/div/div/div[2]/form/div[6]/div/div/input'
        self.generatePasswordBtn        = '/html/body/div[3]/div/div/div[2]/form/div[6]/button'
        self.saveInternalUserBtn        = '/html/body/div[3]/div/div/div[3]/button[2]'
        self.cancelInternalUserBtn      = '/html/body/div[3]/div/div/div[3]/button[1]'


        self.addExternalUserBtn         = '/html/body/div[3]/div/div/div[2]/form/div[1]/label[2]'
        self.userType                   = '/html/body/div[3]/div/div/div[2]/form/div[2]/div/div/select'
        self.firstNameExternalUser      = '/html/body/div[3]/div/div/div[2]/form/div[3]/div/div[1]/div/input'
        self.lastNameExternalUser       = '/html/body/div[3]/div/div/div[2]/form/div[3]/div/div[2]/div/input'
        self.emailExternalUser          = '/html/body/div[3]/div/div/div[2]/form/div[4]/div[1]/div/input'
        self.phoneExternalUser          = '/html/body/div[3]/div/div/div[2]/form/div[4]/div[2]/div/input'
        self.companyExternalUser        = '/html/body/div[3]/div/div/div[2]/form/div[5]/div[1]/div[1]/div/div/input[1]'
        self.jobTitleExternalUser       = '/html/body/div[3]/div/div/div[2]/form/div[5]/div[1]/div[2]/div/input'
        self.userRoleExternalUser       = '/html/body/div[3]/div/div/div[2]/form/div[5]/div[2]/div/div/div/select'
        self.passwordExternalUser       = '/html/body/div[3]/div/div/div[2]/form/div[6]/div/div/input'
        self.genPasswordBtn             = '/html/body/div[3]/div/div/div[2]/form/div[6]/button'
        self.saveExternalUserBtn        = '/html/body/div[3]/div/div/div[3]/button[2]'
        self.cancelExternalUserBtn      = '/html/body/div[3]/div/div/div[3]/button[1]'
        self.companySuggesttion          = '// *[ @ id = "companyId-item-0"]'


        self.addAPIUSerBtn              = '/html/body/div[3]/div/div/div[2]/form/div[1]/label[3]'
        self.emailAPIUser               = '/html/body/div[3]/div/div/div[2]/form/div[4]/div[1]/div/input'
        self.companyAPIUser             = '/html/body/div[3]/div/div/div[2]/form/div[5]/div[1]/div[1]/div/div/input[1]'
        self.subscriptionType           = '/html/body/div[3]/div/div/div[2]/form/div[7]/div/div/select'
        self.authorizationKey           = '/html/body/div[3]/div/div/div[2]/form/div[8]/div/div/div/input'
        self.cancelAPIUser              = '/html/body/div[3]/div/div/div[3]/button[1]'
        self.saveAPIUser                = '/html/body/div[3]/div/div/div[3]/button[2]'



    def get_element_settings_btn(self):
        return self.driver.find_element(By.XPATH, self.settingsBtn)

    def get_element_internalAdmin_btn(self):
        return self.driver.find_element(By.XPATH, self.internalAdminBtn)

    def get_element_companies_btn(self):
        return self.driver.find_element(By.XPATH, self.companiesBtn)

    def get_element_users_btn(self):
        return self.driver.find_element(By.XPATH, self.usersBtn)

    def get_element_internalAdminPortalBody(self):
        return self.driver.find_element(By.XPATH, self.internalAdminPortalBody)


    ############ + New Company ############

    def get_element_addNewCompany_btn(self):
        return self.driver.find_element(By.XPATH, self.newCompanyBtn)

    def get_element_addCompanyName(self):
        return self.driver.find_element(By.XPATH, self.addCompanyName)

    def get_element_addCompanyCity(self):
        return self.driver.find_element(By.XPATH, self.addCompanyCity)

    def get_element_addCompanyState(self):
        return self.driver.find_element(By.XPATH, self.addCompanyState)

    def get_element_addCompanyWebsite(self):
        return self.driver.find_element(By.XPATH, self.addCompanyWebsite)

    def get_element_saveNewCompany(self):
        return self.driver.find_element(By.XPATH, self.saveNewCompanyBtn)

    ####################################

    ############ Search Company ############

    def get_element_searchCompany(self):
        return self.driver.find_element(By.ID, self.companyTextBox)

    def get_element_searchCompanyCity(self):
        return self.driver.find_element(By.ID, self.cityTextBox)

    def get_element_searchCompanyState(self):
        return self.driver.find_element(By.ID, self.stateSelector)

    def get_element_searchCompany_btn(self):
        return self.driver.find_element(By.XPATH, self.searchCompanyBtn)

    ####################################

    ############ + New User ############

    def get_element_addNewUserBtn(self):
        return self.driver.find_element(By.XPATH, self.newUserBtn)

    def get_element_addNewInternalUserBtn(self):
        return self.driver.find_element(By.XPATH, self.addInternalUserBtn)

    def get_element_internalUserName(self):
        return self.driver.find_element(By.XPATH, self.firstNameInternalUser)

    def get_element_internalUserLastName(self):
        return self.driver.find_element(By.XPATH, self.lastNameInternalUSer)

    def get_element_internalUserEmail(self):
        return self.driver.find_element(By.XPATH, self.emailInternalUser)

    def get_element_internalUserPassword(self):
        return self.driver.find_element(By.XPATH, self.generatePasswordBtn)

    def get_element_internalUserSave_Btn(self):
        return self.driver.find_element(By.XPATH, self.saveInternalUserBtn)

    def get_element_internalUserCancel_Btn(self):
        return self.driver.find_element(By.XPATH, self.cancelInternalUserBtn)



    def get_element_addNewExternalUserBtn(self):
        return self.driver.find_element(By.XPATH, self.addExternalUserBtn)

    def get_element_externalUserType(self):
        return self.driver.find_element(By.XPATH, self.userType)

    def get_element_externalUserName(self):
        return self.driver.find_element(By.XPATH, self.firstNameExternalUser)

    def get_element_externalUserLastName(self):
        return self.driver.find_element(By.XPATH, self.lastNameExternalUser)

    def get_element_externalUserEmail(self):
        return self.driver.find_element(By.XPATH, self.emailExternalUser)

    def get_element_externalUserPhone(self):
        return self.driver.find_element(By.XPATH, self.phoneExternalUser)

    def get_element_externalUserCompany(self):
        return self.driver.find_element(By.XPATH, self.companyExternalUser)

    def get_element_userCompanySuggestion(self):
        return self.driver.find_element(By.XPATH, self.companySuggesttion)

    def get_element_externalUserJob(self):
        return self.driver.find_element(By.XPATH, self.jobTitleExternalUser)

    def get_element_externalUserRole(self):
        return self.driver.find_element(By.XPATH, self.userRoleExternalUser)

    def get_element_externalUserPassword(self):
        return self.driver.find_element(By.XPATH, self.genPasswordBtn)

    def get_element_externalUserSave_Btn(self):
        return self.driver.find_element(By.XPATH, self.saveExternalUserBtn)

    def cancelExternalUser_Btn(self):
        return self.driver.find_element(By.XPATH, self.cancelExternalUserBtn)




    def get_element_addNewAPIUser_btn(self):
        return self.driver.find_element(By.XPATH, self.addAPIUSerBtn)

    def get_element_APIUserEmail(self):
        return self.driver.find_element(By.XPATH, self.emailAPIUser)

    def get_element_APIUserCompany(self):
        return self.driver.find_element(By.XPATH, self.companyAPIUser)

    def get_element_APIUSerSubscriptionType(self):
        return self.driver.find_element(By.XPATH, self.subscriptionType)

    def get_element_APIUSerKey(self):
        return self.driver.find_element(By.XPATH, self.authorizationKey)

    def get_element_SaveAPIUSer_btn(self):
        return self.driver.find_element(By.XPATH, self.saveAPIUser)

    def get_element_CancelAPIUSer_btn(self):
        return self.driver.find_element(By.XPATH, self.cancelAPIUser)




    ####################################




    def internalAdmin_portal(self):
        self.get_element_settings_btn().click()
        self.get_element_internalAdmin_btn().click()

        try:
            element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.XPATH, self.internalAdminPortalBody))
            )
        finally:
            self.get_element_companies_btn().click()
            self.addNewcompaniesInternalPortal()
            self.searchCompany()
            self.get_element_users_btn().click()
            self.addNewInternalUser()
            self.addNewExternalUser()
            self.addNewAPIUser()


    def addNewcompaniesInternalPortal(self):
        self.get_element_addNewCompany_btn().click()
        self.get_element_addCompanyName().send_keys(self.companyTest)
        self.get_element_addCompanyCity().send_keys(self.companyCityTest)
        self.get_element_addCompanyState().send_keys(self.companyStateTest)
        self.get_element_addCompanyWebsite().send_keys(self.companyWebsiteTest)
        self.get_element_saveNewCompany().click()
        time.sleep(5)

    def searchCompany(self): ## Search the same company created previously
        self.get_element_searchCompany().send_keys(self.companyTest)
        self.get_element_searchCompanyCity().send_keys(self.companyCityTest)
        self.get_element_searchCompanyState().send_keys(self.companyStateTest)
        time.sleep(5)
        self.get_element_searchCompany_btn().click()
        time.sleep(3)


    def addNewInternalUser(self):
        self.get_element_addNewUserBtn().click()
        self.get_element_addNewInternalUserBtn().click()
        self.get_element_internalUserName().send_keys('QA Test' + str(random.randint(0, 100)))
        self.get_element_internalUserLastName().send_keys('Regression')
        self.get_element_internalUserEmail().send_keys('QA_regression_test_' + str(random.randint(0, 100)) + '@gmail.com')
        self.get_element_internalUserPassword().click()
        time.sleep(5)
        self.get_element_internalUserSave_Btn().click()



    def addNewExternalUser(self):
        self.get_element_addNewUserBtn().click()
        self.get_element_addNewExternalUserBtn().click()

        user_type              = ["Shipper/Receiver",
                                 "Carrier/Driver",
                                 "Broker",
                                 "Corporate",
                                 "3rd Party"]

        user_role               = ["No Role",
                                   "Admin",
                                   "Viewer",
                                   "Company Admin",
                                   "Editor"]

        randUserType = random.randint(0, len(user_type) - 1)
        randUserRole = random.randint(0, len(user_role)-1)

        self.get_element_externalUserType().click()
        time.sleep(0.5)

        self.get_element_externalUserType().send_keys(user_type[randUserType])
        self.get_element_externalUserName().send_keys('QA Test' + str(random.randint(0, 100)))
        self.get_element_externalUserLastName().send_keys('Regression')
        self.get_element_externalUserEmail().send_keys('QA_regression_test_' + str(random.randint(0, 100)) + '@gmail.com')
        self.get_element_externalUserPhone().send_keys(str(random.randint(1111111111, 9999999998)))
        self.get_element_externalUserCompany().send_keys('Omnitracs Regression Test')
        time.sleep(3)
        self.get_element_userCompanySuggestion().click()
        self.get_element_externalUserJob().send_keys('QA Engineer')
        self.get_element_externalUserRole().send_keys(user_role[randUserRole])
        self.get_element_externalUserPassword().click()
        time.sleep(5)
        self.get_element_externalUserSave_Btn().click()




    def get_random_string(self):
        # choose from all lowercase letter
        lowerCaseletters                = string.ascii_lowercase
        upperCaseLetters                = string.ascii_uppercase
        numbers                         = string.digits

        result_str = ''.join(random.choice(lowerCaseletters + upperCaseLetters + numbers)for i in range(40))
        return result_str

    def addNewAPIUser(self):
        self.get_element_addNewUserBtn().click()
        self.get_element_addNewAPIUser_btn().click()

        subscriptionType                    = ['Address Validation',
                                               'Location Details',
                                               'Location Analytics']

        randomsubscriptionType = random.randint(0, len(subscriptionType) - 1)


        self.get_element_APIUserEmail().send_keys('QA_regression_test_' + str(random.randint(0, 100)) + '@gmail.com')
        self.get_element_APIUserCompany().send_keys('Omnitracs Regression Test')
        time.sleep(3)
        self.get_element_userCompanySuggestion().click()
        self.get_element_APIUSerSubscriptionType().send_keys(subscriptionType[randomsubscriptionType])
        self.get_element_APIUSerKey().send_keys(self.get_random_string())
        time.sleep(5)

        self.get_element_SaveAPIUSer_btn().click()




