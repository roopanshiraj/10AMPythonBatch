print("Enter any number of terms")
n= int(input())
t1=0
t2=1
print("Fibonacci series of",n, "numbers is")
for i in range (1, n+1):
    print(t1,",")
    sum=t1+t2
    t1=t2
    t2=sum

