class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
        self.account = BankAccount(0.02, 0)
    
    def display_info(self):
        print("--------------------------------")
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"{self.first_name} has {self.gold_card_points} points!")
        print("--------------------------------")
    

    def enroll(self):
        if self.is_rewards_member != False:
            print('User already a Member')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200

    def spend_points(self, amount):
        if amount > self.gold_card_points:
            print("Not enough points!")
        else:
            self.gold_card_points -= amount
    
    def make_deposit(self, amount):
        self.account.balance += amount
        return self.account.balance

    def make_withdrawl(self, amount):
        self.account.balance -= amount
        return self.account.balance
    
    def display_user_account_balance(self):
        print("-------------------")
        print(self.account.balance)
        print("-------------------")


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

user = User("Casey", "DEon", "cdeon731@gmail.com", "28")
user.make_deposit(100)
user.make_withdrawl(50)
user.display_user_account_balance()
