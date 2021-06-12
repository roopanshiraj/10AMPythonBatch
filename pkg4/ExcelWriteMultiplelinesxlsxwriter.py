import xlsxwriter
wk= xlsxwriter.Workbook("C://Users//roops//OneDrive//Desktop//ExcelWrite2.xlsx")
sh= wk.add_worksheet('Sheet1')
contentt=['my','name','is','Roopanshi','Welcome','to','everyone','of','you']
row=0
col=0

for item in contentt:
    sh.write(row,col,item)
  #  row=row+1
    col=col+1
wk.close()