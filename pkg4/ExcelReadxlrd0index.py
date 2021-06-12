import xlrd
location=("C://Users//roops//OneDrive//Desktop//ExcelRead.xls")
work=xlrd.open_workbook(location)
sheet=work.sheet_by_index(0)
print(sheet.cell_value(0,0))