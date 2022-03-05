s=lambda a:a*a
r=lambda q,r:q*r
t=lambda l,b,h:l*b*h/2
x=int(input("enter the side of square"))

l=int(input("enter the length of rectangle"))
c=int(input("enter the breadth of the rectangle"))

x=int(input("enter the length of triangle"))
y=int(input("enter the height of triangle"))
z=int(input("enter the base of triangle"))

print("The area of square is",s(x))

print("the area of rectangle is",r(l,c))

print("the area of triangle is",t(x,y,z))
