import xlwt

wk=xlwt.Workbook()
sh=wk.add_sheet('Sheet_1')
sh.write(1,0,'Roopanshi')
wk.save("C://Users//roops//OneDrive//Desktop//ExcelWrite.xls")