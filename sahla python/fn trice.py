a=int(input("enter first number"))
b=int(input("enter second number"))
c=int(input("enter third number"))
def sum_of_3(a,b,c):
    s=a+b+c
    if(a==b==c):
        return(3*s)
    else:
        return(s)
print("sum=",sum_of_3(a,b,c))    
