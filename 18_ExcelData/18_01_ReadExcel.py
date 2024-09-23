# Import package
import openpyxl

# Load Workbook
wk = openpyxl.load_workbook("C:\\Users\\a315707\\OneDrive - Deutsche Telekom AG\\Schulungen\\Programmierung\\Python\\PythonLearning\\18_ExcelData\\TestData.xlsx")

print(wk.sheetnames) # List sheets
print(wk.active.title) # Active Sheet

# Create object of sheet on which you want to work

sh = wk['Tabelle1']
print(sh.title)
