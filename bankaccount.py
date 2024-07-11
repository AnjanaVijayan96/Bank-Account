
class bank_account:
    def __init__(self):
        self.amount=0
    def login(self):
        account_login=int(input("Enter your Account Number:"))
    def password(self):
        account_passward=int(input("Enter your Password:"))
        print("Login Successfully")
    def deposit(self):
        amt=float(input("Enter your Amount : "))
        self.amount+= amt
        print("Amount successfully Deposited",amt)
    def withdraw(self):
        amt=float(input("Enter your Withdrawal Amount : "))
        if(self.amount>=amt):
            self.amount-=amt
            print("Amount Successfully Debited",amt)
        else:
            print("Insufficient Bank balnce.\n You have to keep atleast Rs.500 in your Account ")
    def display(self):
        print("Your Bank Balance is : ",self.amount)

b1=bank_account()
b1.login()
b1.password()
b1.deposit()
b1.withdraw()
b1.display()










