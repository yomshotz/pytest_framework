from Driver.selenium_driver import SeleniumDriver


class Driver_Mapping(SeleniumDriver):

    def __init__(self, driver):
        super(Driver_Mapping, self).__init__(driver)
        self.driver = driver

    # Execute the keyword functions and return the status
    def execute_keyword(self, keyword, attribute, value, objectname):
        
        self.keyword = keyword.lower

        if self.keyword == "navigate":
            result = self.navigate(value)
            return result
        elif self.keyword == "input":
            result = None
            result = self.sendKeys(value, objectname)
            return result
        elif self.keyword == "click":
            result = None
            result = self.elementClick(objectname)
            return result
        elif self.keyword == "wait":
            result = None
            result = self.wait(value)
            return result
        elif self.keyword == "select_checkbox":
            result = None
            result = self.select_checkbox(objectname, value)
            return result
        elif self.keyword == "select_dropdown":
            result = None
            result = self.select_dropdown(objectname, value)
            return result
        elif self.keyword == "unselect_checkbox":
            result = None
            result = self.unselect_checkbox(objectname, value)
            return result
        elif self.keyword == "select_radio":
            result = None
            result = self.select_radio(objectname, value)
            return result
        elif self.keyword == "scroll":
            result = None
            result = self.webScroll(value)
            return result
        elif self.keyword == "verify":
            result = None
            result = self.verify(attribute, value, objectname)
            return result
        elif self.keyword == "moveto":
            result = None
            result = self.moveto(objectname)
            return result
        elif self.keyword == "waitfor":
            element_wait = self.waitforelement(value)
            if element_wait:
                return True
            elif element_wait is None:
                return False
            else:
                return False
        elif self.keyword == 'snapshot':
            result = None
            result = self.capturescreen()
            return result
        elif self.keyword == "dragto":
            result = None
            result = self.dragndrop(objectname, value)
            return result
        elif self.keyword == "closebrowser":
            result = None
            result = self.closebrowser()
            return result
        elif self.keyword == "switchto":
            result = None
            result = self.switchto(attribute, value)
            return result
        elif self.keyword == "waitfor":
            result = None
            result = self.waitforelement(objectname)
            return result
        elif self.keyword == "savedata":
            result = None
            result = self.savedata(objectname, value)
            return result
        elif self.keyword == "getdbvalue":
            result = None
            result = self.getdbvalue(value)
            return result
        elif self.keyword == "compare":
            result = None
            result = self.compare()
            return result
        elif self.keyword == "doubleclick":
            result = None
            result = self.doubleClick(objectname)
            
            return result
        # elif self.keyword == "dbconnect":
        #     result = None
        #     result = self.dbconnect()
        #     return result
        # elif self.keyword == "draftquery":
        #     result = None
        #     result = self.draftquery(value)
        #     return result
        # elif keyword == "concat":
        #     result = None
        #     result = self.concat(value)
        #     return result
        # elif keyword == "executequery":
        #     result = None
        #     result = self.executequery()
        #     return result
        else:
            print("Bad keyword or not found. All keywords should be in lowercase!!")
            return False