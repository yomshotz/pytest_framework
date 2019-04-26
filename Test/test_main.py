import pytest
import time
from Utilities.xlutil import ExcelUtil
from Utilities.Constants import Constants
from Utilities.module_mapping import Driver_Mapping()

@pytest.mark.usefixtures("invoke_browser")
class Test_Main:

    @pytest.fixture(autouse=True)
    def initialSetup(self, invoke_browser):
        self.constants = Constants()
        self.excel = ExcelUtil()
        self.drivermethod = Driver_Mapping(self.driver)

    @pytest.mark.run(order=1)
    def test_initialize(self):
        self.excel.setExcelFile(self.constants.Path_TestData)
        self.execute_testCases()

        # driver = self.driver
        # print(driver.title)

        # time.sleep(2)

    def execute_testCases(self):
        ntotalTestCases = self.excel.getRowCount(
            self, 
            self.constants.Sheet_TestCases
        )





