n=int(input("enter the number"))
s=a=0
while (n>0):
       a=n%10
       s=s+a
       n=n//10
print("sum=",s)
