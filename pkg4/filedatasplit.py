f=open("C://Users//roops//OneDrive//Desktop//first.txt", "r")
data= f.readlines()
for line in data:
    word=line.split()
    print(word)
