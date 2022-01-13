str=list("malyalam")
for i in str:
    c=0
    if (i!=" "):
        for j in range(0, len(str)):
            if(i==str[j]):
                c=c+1
                str[j]=' '
        print(i,"=",c)
