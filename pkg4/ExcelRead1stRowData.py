import xlrd
location=("C://Users//roops//OneDrive//Desktop//ExcelRead.xls")
work=xlrd.open_workbook(location)
sheet=work.sheet_by_index(0)

for i in range(sheet.ncols):
    print(sheet.cell_value(0,i))