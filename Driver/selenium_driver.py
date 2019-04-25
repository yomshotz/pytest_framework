from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains
from Utilities.constant import Constants
import time

class SeleniumDriver():

    def __init__(self, driver):
        self.driver = driver
        self.constants = Constants()
        self.UIvalue = None

    def navigate(self, datavalue):
        try:
            self.driver.get(datavalue)
            return True
        except:
            print("Navigation failed")

    def getelement(self, locator):
        try:
            element = self.driver.find_element(By.XPATH, locator)
        except:
            print("Element not found")

        return element

    def findelement(self, locator):
        try:
            element_to_find = None

            element_to_find = self.driver.find_elements(By.XPATH, locator)

            if len(element_to_find) > 0:
                return True
            else:
                return False

    def waitforelement(self, locator):
        try:
            element_to_wait = None
            nwait = None

            nwait = WebDriverWait(
                self.driver, 
                10, 
                poll_frequency=1,
                ignored_exceptions=[
                    NoSuchElementException,
                    ElementNotVisibleException,
                    ElementNotSelectableException
                ]
            )

            element_to_wait = nwait.until(EC.presence_of_all_elements_located(
                (By.XPATH, locator)
            ))

    def elementClick(self, locator):
        try:
            self.getelement(locator).click()
            return True
        except:
            print("Element not clicked")

    def sendKeys(self, data, locator):
        try:
            self.getelement(locator).clear()
            self.getelement(locator).send_keys(data)
            return True
        except:
            print("Cannot send data to the element field")
            return False

    def capturescreen(self):

        try:
            filename = "Scrnshot"+"_"+str(round(time.time()*1000))+".png"
            folder_location = self.constants.path_Snapshot
            destination = folder_location+filename
            self.driver.save_screenshot(destination)
            return True
        except NotADirectoryError:
            print("Capture screenshot failed")
            return False
    
    def getTitle(self):
        return self.driver.title

    def webScroll(self, direction):

        try:
            if direction == 'up':
                self.driver.execute_script("window.scrollBy(0,-1000);")
                return True
            elif direction == 'down':
                self.driver.execute_script("window.scrollBy(0,1000);")
                return True
            elif disrection == 'right':
                self.driver.execute_script("window.scrollBy(1000,0);")
                return True
            else:
                self.driver.execute_script("window.scrollBy(-1000,0);")
                return True
        except:
            print("Scrolling failed")
            return False

    def select_dropdown(self, locator, value):
        try:
            drop_down = self.driver.find_element(By.XPATH, locator)
            sel_element = Select(drop_down)
            sel_element.select_by_value(value)
            return True
        except:
            print("Dropdown selection failed")
            return False

    def select_radio(self, locator, datavalue):
        try:
            ulocator = locator.format(datavalue)
            nradio = self.driver.find_element(By.XPATH, ulocator)
            nradio.click()
            ulocator = ""
            return True
        except:
            print("Select radio button failed")
            return False

    def select_checkbox(self, locator, datavalue):
        try:
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(By.XPATH, ulocator)
            isSelected = ncheckbox.is_selected()
            if not isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            print("Select checkbox failed")
            return False
    
    def unselect_checkbox(self, locator, datavalue):
        try:
            ulocator = locator.format(datavalue)
            ncheckbox = self.driver.find_element(By.XPATH, ulocator)
            isSelected = ncheckbox.is_selected()
            if isSelected:
                ncheckbox.click()
                ulocator = ""
                return True
        except:
            print("Unselect of checkbox failed")
            return False

    def wait(self, datavalue):
        try:
            nseconds = int(float(datavalue))
            time.sleep(nseconds)
            return True
        except:
            self.log.error("Wait for failed")
            return False

    # Method to verify Text, enabled, selected, displayed, exists, title
    def verify(self, property, value, locator):
        try:
            if property == "text":
                UI_Text = None
                UI_Text = self.driver.find_element(
                    By.XPATH, locator).text
                if str(UI_Text) == str(value):
                    return True
                else:
                    return False
            elif property == "enabled":
                enable_flag = None
                enable_flag = self.driver.find_element(
                    By.XPATH, locator).is_enabled()
                if str(enable_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "selected":
                select_flag = None
                select_flag = self.driver.find_element(
                    By.XPATH, locator).is_selected()
                if str(select_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "displayed":
                display_flag = None
                display_flag = self.driver.find_element(
                    By.XPATH, locator).is_displayed()
                if str(display_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "exists":
                exist_flag = None
                exist_flag = self.findelement(locator)
                if str(exist_flag) == str(value):
                    return True
                else:
                    return False
            elif property == "title":
                title = str(self.getTitle())
                if title == value:
                    return True
                else:
                    return False

        except:
            self.log.error("Verify failed")
            return False

    def moveto(self, locator):
        try:
            element = None
            element = self.driver.find_element(By.XPATH, locator)
            action = ActionChains(self.driver)
            action.move_to_element(element).perform()
            return True
        except:
            print("Cursor Move to element failed")
            return False

    # Method to drag and drop element from source to destination
    def dragndrop(self, locator, value):
        try:
            from_element = self.driver.find_element(By.XPATH, locator)
            to_element = self.driver.find_element(By.XPATH, value)
            action = ActionChains(self.driver)
            action.drag_and_drop(from_element, to_element).perform()
            return True
        except:
            print("Drag and drop failed")
            return False