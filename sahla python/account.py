class Bank:
 def _init_(self):
   self.balance=0
   print("__Create an Account__")
   self.name=input("Enter the name :")
   self.acctno=int(input("Enter the account number :"))
   self.typeofac=input("Enter the type of account :")
 def deposit(self):
            amount=int(input("Enter the amount to be deeposit:"))
            self.balance+=amount
            print("Amount deposited:",amount)
 def withdraw(self):
            amount=int(input("Entyer the amount withdrawn:"))
            if self.balance>=amount:
                self.balance-=amount
                print("Amount withdrawn:",amount)
            else:
                print("insuffient balance!")
 def display(self):
             print("Account Balance :",self.balance)
a=Bank()
a._init_()
while(1):
        print("\n1.Deposit\n2.Withdrawal\n3.Balance\n4.Exit\n")
        ch=int(input("Enter your choice :"))
        if ch==1:
            a.deposit()
        elif ch==2:
            a.withdraw()
        elif ch==3:
            a.display()
        else:
            print("Wrong Choice!")
            exit()
        
