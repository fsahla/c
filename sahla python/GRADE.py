x=int(input("enter the marks of ads"))
y=int(input("enter the marks of ase"))
z=int(input("enter the marks of mfc"))
r=int(input("enter the marks of ads"))
l=int(input("enter the marks of html"))
total=x+y+z+r+l
print("total",total)
average=total/5
print("average=",average)
if(average>70):
    print ("A GRADE")
elif(average>60):
 print ("B GRADE")
elif(average>50):
 print ("C GRADE")
else:
    print ("fail")
