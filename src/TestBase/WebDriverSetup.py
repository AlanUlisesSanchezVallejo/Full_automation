import unittest
from selenium import webdriver
import urllib3
from selenium.webdriver.chrome.service import Service

class WebDriverSetup(unittest.TestCase):
    def setUp(self):
        service_chrome = Service ("C:\dchrome\chromedriver.exe")
        self.driver = webdriver.Chrome(service = service_chrome)
        self.driver.maximize_window()


    def tearDown(self):
        self.driver.close()