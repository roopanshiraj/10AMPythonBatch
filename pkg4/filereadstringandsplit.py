f=open("C://Users//roops//OneDrive//Desktop//first.txt", "r")
data=f.readlines()
for i in data:
    print(i)
    word=i.split()
    print(word)
    print(len(word))