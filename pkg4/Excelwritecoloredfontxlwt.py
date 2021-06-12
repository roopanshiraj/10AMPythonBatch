import xlwt

wk=xlwt.Workbook()
sh=wk.add_sheet('Sheet_1')
style=xlwt.easyxf('font:bold 1,color red;')
sh.write(0,0,'Roopanshi',style)
wk.save("C://Users//roops//OneDrive//Desktop//ExcelWrite.xls")