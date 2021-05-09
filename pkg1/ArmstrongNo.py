print("Enter any number")
num= int(input())
temp=num
sum=0
while(num>0):
    rem=num%10
    sum=sum+(rem*rem*rem)
    num=num//10
if(temp==sum):
    print("Number is armstrong")
else:
    print("Number is not armstrong")
