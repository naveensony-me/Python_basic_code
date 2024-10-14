# WAP to find the greatest of 4 number entered by the user.

num1=int(input("Enter 1st Number: "))
num2=int(input("Enter 2nd Number: "))
num3=int(input("Enter 3rd Number: "))
num4=int(input("Enter 4rd Number: "))

if(num1>=num2 and num1>=num3 and num1>=num4):
    print("Number 1 is largest")

elif(num2>=num3 and num2>=num4 and num2>=num1):
    print("Number 2 is largest")

elif(num3>num4 and num4>=num1 and num4>=num2):
    print("Number 3 is largest")

else:
    print("Number 4 is largest")




