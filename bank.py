class Bank:

    def __init__(self,name,balance,account_no):
        self.name = name
        self.balance = balance
        self.account_no = account_no
        print("\nAccount Holder :",name)
        print("Account balance :",balance)
        print("Account number :",account_no)



    def debit(self,amount):
        if amount <= self.balance:
            self.balance -= amount
            print("\nAmount withdraw :",amount)
            print("Remaining Balance :",self.balance)
        else:
            print("\nInsuficient Balance")

    def credit(self,amount):
        if amount > 0:
            self.balance += amount
            print("\nAmount Credited :",amount)
            print("Total Balance :",self.balance)



    def display_detail(self):
        print("\nCurrent balance :",self.balance)
        
 

user1 = Bank("Rahul",4000,324174)
user1.debit(400)
user1.credit(1000)

user2 = Bank("Aman",5000,369852)
user2.credit(2000)

