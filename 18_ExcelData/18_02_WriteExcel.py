import openpyxl
import openpyxl.workbook

wk = openpyxl.Workbook()
sh = wk.active
sh.title="HelloTestingWorld"
sh['A4'].value="www.theTestingWorld.com"
wk.create_sheet(title="TestingW")
sh1=wk['TestingW']
sh1['A3']="+918743913121"

# Remove Sheet

#wk.remove_sheet(wk['HelloTestingWorld'])
wk.remove(wk['HelloTestingWorld'])

wk.save("C:\\Users\\a315707\\OneDrive - Deutsche Telekom AG\\Schulungen\\Programmierung\\Python\\PythonLearning\\18_ExcelData\\18_02_OutputExcel.xlsx")

