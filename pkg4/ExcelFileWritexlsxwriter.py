import xlsxwriter
wk= xlsxwriter.Workbook("C://Users//roops//OneDrive//Desktop//ExcelWrite1.xlsx")
sh= wk.add_worksheet('Sheet_1')
sh.write('A1','Deepak')
sh.write('B1','Chanana')
wk.close()
