import pytest
import time
import unittest
from Utilities.xlutil import ExcelUtil
from Utilities.constant import Constants
from Utilities.module_mapping import Driver_Mapping

@pytest.mark.usefixtures("invoke_browser")
class Test_Main(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def initialSetup(self, invoke_browser):
        self.constants = Constants()
        self.excel = ExcelUtil()
        self.drivermethod = Driver_Mapping(self.driver)

    @pytest.mark.run(order=1)
    def test_initialize(self):
        self.excel.setExcelFile(self.constants.path_TestData)
        self.execute_testCases()

    def execute_testCases(self):
        ntotalTestCases = self.excel.getRowCount(
            self.constants.Sheet_TestCases
        )

        for ntestCases in range(1, (ntotalTestCases-1)):
            nTestCaseID = self.excel.getCellData(
                self.constants.Sheet_TestCases,
                ntestCases,
                self.constants.Col_TestCaseID
            )

            nTestCaseDescription = self.excel.getCellData(
                self.constants.Sheet_TestCases,
                ntestCases,
                self.constants.Col_TestCaseDescription
            )

            nRunMode = self.excel.getCellData(
                self.constants.Sheet_TestCases,
                ntestCases,
                self.constants.Col_RunMode
            )

            if nRunMode == 'Yes':
                testsheet_name = nTestCaseID

                test_iterations = self.excel.getTestIterations(
                    nTestCaseID, 
                    testsheet_name
                )

                print("Number of test iterations: "+str(test_iterations-1))

                print("******************************************************")
                print("Test case: " + str(nTestCaseID) + ":" + str(nTestCaseDescrption))
                print("******************************************************")

                for nTest in range(1, test_iterations):
                    nStartStep = self.excel.getRowContains(
                        nTestCaseID, 
                        self.constants.Col_TestCaseID,
                        self.constants.Sheet_TestSteps
                    )
                    
                    nEndStep = self.excel.getTestStepsCount(
                        self.constants.Sheet_TestSteps,
                        nTestCaseID,
                        nStartStep
                    )

                    for step in range(nStartStep, nEndStep):
                            
                        ntestStepId = self.excel.getCellData(
                            self.constants.Sheet_TestSteps,
                            step,
                            self.constants.Col_TestScenarioID,
                        )
                        
                        nstepDescription = self.excel.getCellData(
                            self.constants.Sheet_TestSteps,
                            step,
                            self.constants.Col_TestDescription,
                        )
                        
                        nObject = self.excel.getCellData(
                            self.constants.Sheet_TestSteps,
                            step,
                            self.constants.Col_PageObject,
                        )
                        
                        nObject_Value = self.excel.getObjectValue(
                            self.constants.Sheet_Objectvalue,
                            nObject
                        )
                        
                        nActionKeyword = self.excel.getCellData(
                            self.constants.Sheet_TestSteps,
                            step, 
                            self.constants.Col_ActionKeyword,
                        )
                        
                        nProperty = self.excel.getCellData(
                            self.constants.Sheet_TestSteps,
                            step, 
                            self.constants.Col_ObjProperty,
                        )

                        if nActionKeyword == "dragto" or nActionKeyword == "waitfor":
                            tempdata = self.excel.getCellData(
                                self.constants.Sheet_TestSteps,
                                step, 
                                self.constants.Col_Datavalue,
                            )
                            ndataValue = self.excel.getObjectValue(
                                self.constants.Sheet_Objectvalue,
                                tempdata
                            )
                        else:
                            ndataValue = self.excel.getCellData(
                                self.constants.Sheet_TestSteps,
                                step, 
                                self.constants.Col_Datavalue,
                            )
                        
                        testdata_value = self.excel.getTestdatavalue(
                            nTestCaseID,
                            ndataValue,
                            ntest
                        )

                        if testdata_value is None:
                            testdata_value = ndataValue
                        else:
                            testdata_value = testdata_value