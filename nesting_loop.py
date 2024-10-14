# To Perform nested loop (loop inside loop)

age=int(input("Enter your age: "))

if(age>=18):
    if(age>=80):
        print("old person not allow to drive")
    else:
        print("Can drive")
else:
    print("Cannot drive")