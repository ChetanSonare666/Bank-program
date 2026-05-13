class Bank:
    
    def __init__(self,name,account_no,balance):
        self.name = name
        self.account_no = account_no
        self.balance = balance
        
        print("\nAccount Holder Name:",name)
        print("Account Number :",account_no)
        print("Current Balance :",balance,"\n")
        
    def debit(self,amount):
            self.amount = amount
            if self.balance >= amount:
                self.balance-= amount
                print("Amount Debited :",amount,"\n")
            else:
                print("Insufficient Balance")
            
    def credit(self,amount):
            self.amount = amount
            if amount > 0:
                self.balance += amount
                print("Amount Credited",amount,"\n")
            else:
                print("Invalid Amount")
                
    def display_detail(self):
            print("Total amount remaining :",self.balance,"\n")

person = int(input("Enter the number of user :"))

for i in range(1,person+1):

    print("\n","For person",i)

    name = str(input("Enter Account Holder Name :"))
    account_no = str(input("Enter Your Account Number :"))
    balance = int(input("Enter The Balance :"))

    debit = int(input("Enter the amount to debit :"))

    credit = int(input("Enter the amount to credit :"))

    user1 = Bank(name,account_no,balance)
    user1.debit(debit)
    user1.credit(credit)
    user1.display_detail()


                
    