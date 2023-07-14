num1=float(input("enter your number "))
operation=input("enter the operation that you want to perform ")
num2=float(input("enter your other number "))
if operation=="+":
    print(num1+num2)
elif operation=="-":
    print(num1-num2)
elif operation=="*":
    print(num1*num2)
elif operation=="/":
    print(num1/num2)
else:
    print("invalid operation")