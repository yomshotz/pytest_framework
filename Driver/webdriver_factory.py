from selenium import webdriver
from Utilities.constant import Constants
import os

class GetWebdriverInstance():
    ### Browser value is retrieved from request variable in conftest
    def __init__(self, browser):
        self.browser = browser
        self.constants = Constants()

    def getbrowserInstance(self):
        if self.browser == 'IE':

            driver_location = self.constants.path_IE_driver
            os.environ["webdriver.IE.driver"] = driver_location
            driver = webdriver.Ie(driver_location)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        elif self.browser == 'chrome':

            driverLocation = self.constants.path_chrome_driver
            os.environ["webdriver.chrome.driver"] = driverLocation
            driver = webdriver.Chrome(driverLocation)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        elif self.browser == 'firefox':

            path = self.constants.path_firefox_driver
            driver = webdriver.Firefox(executable_path=path)
            driver.maximize_window()
            driver.implicitly_wait(5)
            driver.delete_all_cookies()

        return driver