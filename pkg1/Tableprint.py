print("Enter any number")
num=int(input())
print("Table of" ,num, "is ")
for i in range(1,11):
    table=num*i
    print(num, "*" , i , "=" , table)