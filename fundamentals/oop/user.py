class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}")
        print(f"Last Name: {self.last_name}")
        print(f"Email: {self.email}")
        print(f"Age: {self.age}")
        print(f"Rewards Member: {self.is_rewards_member}")
        print(f"Gold Card Points: {self.gold_card_points}")
    
    def enroll(self):
        if self.is_rewards_member == True:
            print('User already a Member')
        else:
            self.is_rewards_member = True
            self.gold_card_points = 200
    
    def spend_points(self, amount):
        if amount > self.gold_card_points:
            return False
        self.gold_card_points -= amount

my_user = User("Casey", "DEon", "cdeon731@gmail.com", 28)
my_user.display_info()
my_user.enroll()
my_user.spend_points(100)
my_user.display_info()