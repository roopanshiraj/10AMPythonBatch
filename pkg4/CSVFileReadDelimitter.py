import csv
with open('C://Users//roops//OneDrive//Desktop//File1.csv','r') as file:
    reader= csv.reader(file, delimiter='\t')
    for row in reader:
       print(row)