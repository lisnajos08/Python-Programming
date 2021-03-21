class Bank_Account:
    def __init__(self):
        self.balance = 0
        print("Hello!!! Welcome")
        self.name = input("Enter your name : ")
        self.ac_no = input("Enter Account Number : ")
        self.type = input("Enter Account Tyoe : ")

    def deposit(self):
        amount = float(input("Enter amount to be Deposited: "))
        self.balance = self.balance + amount
        print("\n Amount Deposited:", amount)

    def withdraw(self):
        amount = float(input("Enter amount to be Withdrawn: "))
        if self.balance >= amount:
            self.balance = self.balance - amount
            print("\n You Withdrew:", amount)
        else:
            print("\n Insufficient balance  ")

    def display(self):
        print(self.name, ", Net Available Balance=", self.balance)


s = Bank_Account()

s.deposit()
s.withdraw()
s.display()