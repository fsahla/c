a=int(input("enter the first number"))
b=int(input("enter the second number"))
def arithematic_operations(a,b):
    s=a+b
    m=a*b
    d=a-b
    div=a/b
    return(s,m,d,div)
l=arithematic_operations(a,b)
print("sum=",l[0])
print("product=",l[1])
print("difference",l[2])
print("division",l[3])
