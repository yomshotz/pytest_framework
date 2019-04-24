import openpyxl

class ExcelUtil:
    
    def setExcelFile(self, path):
        try:
            self.workbook = openpyxl.load_workbook(file)
        except:
            print('Failed to open the file')

    def getRowCount(self, sheetName):
        try:
            self.sheet = ""
            
            self.sheet = self.workbook.get_sheet_by_name(sheetName)
            return sheet.max_row
        except:
            print('Failed to get total row count')

    def getColCount(self, sheetName):
        try:
            self.sheet = ""

            self.sheet = self.workbook.get_sheet_by_name(sheetName) 
            return sheet.max_column
        except:
            print('Failed to get total column count')

    def getCellData(self, sheetName, row_count, col_count):
        try:
            self.sheet = ""                

            self.sheet = self.workbook.get_sheet_by_name(sheetName)

        return sheet.cell(row=row_count, column=col_count).value

    def getRowContains(self, testname, colNum, sheetname):
        rowNum = 0
        try:
            rowCount=0
            rowCount = self.getRowCount(sheetname)

            for rowNum in range(0, rowCount):
                if self.getCellData(sheetname, rowNum, colNum) == testname:
                    break
        except:
            print('Failed to get total column count')

    


    def writeData(file, sheetName, row_count, col_count, data):
        workbook = openpyxl.load_workbook(file)
        sheet = workbook.get_sheet_by_name(sheetName)
        sheet.cell(row=row_count, column=col_count).value = data
        workbook.save(file)