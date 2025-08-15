n=151
sum=0
order=len(str(n))
copy=n
while(n>0):
    
    digit=n%10 
    sum+=digit**order
    n=n//10

if (sum==copy):
    print(f"{copy}Number is an armstrong number")


else:
    print(f"{copy}Number is not armstrong number")