import csv
csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('C://Users//roops//OneDrive//Desktop//File3.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)