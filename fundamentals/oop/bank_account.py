class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance

    def display_account_info(self):
        print("--------------------------")
        print(f"Current Balance: {self.balance}")
        print("--------------------------")

    def deposit(self, amount):
        self.balance += amount
        return self
        
    def withdraw(self, amount):
        self.balance -= amount
        if self.balance < 0:
            self.balance -= 5
            print("Insufficient funds: Charging $5 fee")
        else:
            return self
        
    def yield_interest(self):
        if self.balance < 0:
            return False
        interest = self.balance * self.int_rate
        new_balance = interest + self.balance
        self.balance = new_balance
        return new_balance

account1 = BankAccount(.01, 400)
account2 = BankAccount(.01, 20)

account1.deposit(25)
account1.deposit(25)
account1.deposit(25)
account1.withdraw(100)
account1.yield_interest()
account1.display_account_info()

account2.deposit(100)
account2.deposit(30)
account2.withdraw(50)
account2.withdraw(50)
account2.withdraw(50)
account2.withdraw(50)
account2.yield_interest()
account2.display_account_info()