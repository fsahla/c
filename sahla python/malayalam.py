x=int(input("enter a string"))
for i in x:
 if(i!="#"):
  c=0
for j in range(0,len(x)):
  if (i==str[j]):
      c=c+1
      str[j]="#"
print(1,"=",c)

