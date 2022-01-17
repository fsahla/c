l1=list(input("enter the list of first"))
l2=list(input("enter the list of second"))
def functionlist(l1,l2):
    c=0
    for i in l1:
        for j in l2:
            if(i==j):
                return(True)
if(functionlist(l1,l2)):
    print("common elements exist")
else:
    print("common elements doesnot exist")
