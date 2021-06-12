f=open("C://Users//roops//OneDrive//Desktop//first.txt", "r")
data=f.readlines()
for i in data:
    word= i.split()
    for j in range (len(word)):
        print(word[j])
