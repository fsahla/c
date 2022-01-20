n=int(input("enter a value:"))
def neon(b):
         s=a=0
         q=(b**2)
         while(q>0):
             a=q%10
             s=s+a
             q=q//10
         if(s==b):
            print("The inputed number is neon")
         else:
            print("the inputed number is not neon")
neon(n)
