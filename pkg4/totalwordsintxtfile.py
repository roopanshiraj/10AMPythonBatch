f=open("C://Users//roops//OneDrive//Desktop//first.txt", "r")
data=f.readlines()
lines=0
for i in data:
    lines=lines+1
print("lines count", lines)