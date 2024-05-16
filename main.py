'''

Welcome to GDB Online.
GDB online is an online compiler and debugger tool for C, C++, Python, Java, PHP, Ruby, Perl,
C#, OCaml, VB, Swift, Pascal, Fortran, Haskell, Objective-C, Assembly, HTML, CSS, JS, SQLite, Prolog.
Code, Compile, Run and Debug online from anywhere in world.

'''
print("welcome to SBI bank")
class sbibank:
    def __init__(self,name,DOB, accountnumber,ifscCode,balance ):
        self.name=name
        self.DOB=DOB
        self.accountnumber=accountnumber
        self.ifscCode=ifscCode
        self.balance=balance
    def deposit (self, ammount):
        self.balance +=ammount
    def withdraw (self,ammount):
        self.balance -=ammount
    def checkbalance (self ):
        print("your balance is",self.balance)
obj1=sbibank('tarun',"22/04/2005",12345678,54321,50000)
#print(obj1.name)  you declare your own like  'obj1.z'  and print(obj1.z) like that only ok...
#print(obj1.accountnumber)
print("1.user_details\n2.Deposite\n3.Withdraw\n4.Checkbalance\n5.END")
opt=input("enter your option:")
if opt=='1':
    print("Name=",obj1.name)
    print("Date of birth=",obj1.DOB)
    print("accountnumber=",obj1.accountnumber)
    print("IFSC code=",obj1.ifscCode)
elif opt=='2':
    d=float(input('how much amount you want to deposite:'))
    obj1.deposit(d)
    print("amount deposited successfully \n")
    obj1.checkbalance()
elif opt=='3':
    obj1.checkbalance()
    w=int(input('enter how much amount you want to withdraw:'))
    obj1.withdraw(w)
    print("amount withdraw successfully\n")
    obj1.checkbalance()
else:
    obj1.checkbalance()
 
while(opt!='5'):
    print("__________________")
    print("again you want any help:")
    print("1.user_details\n2.Deposite\n3.Withdraw\n4.checkbalance\n5.END")
    opt=input("enter your option:")
    
    
print("Thanking  you")





