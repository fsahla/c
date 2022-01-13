x=int(input("enter the number"))
i=1
c=0
while(i<=x):
     if(x%i==0):
         c=c+1
     i=i+1
if(c==2):
    print(" the number is prime no")
else:
    print("The number is not prime no")
     
