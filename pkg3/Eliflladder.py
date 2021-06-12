print("Please enter the value of marks")
marks=int(input())
if((marks>0)and(marks<35)):
    print("Fail")
elif((marks>=35)and(marks<60)):
    print("Pass")
elif((marks>=60)and(marks<80)):
    print("First Division")
elif((marks>=80)and(marks<100)):
    print("Merit")
else:
    print("Please enter correct marks")