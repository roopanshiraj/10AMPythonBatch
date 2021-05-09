print("Enter any number")
num=int(input())
if (num > 1):
    for i in range(2, num//2):
        if (num % i == 0):
            print("Number is not a prime number")
            break
    else:
        print("Number is a prime number")
else:
    print("Enter correct number")




