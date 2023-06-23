class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0
    
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

my_user = User("Casey", "DEon", "cdeon731@gmail.com", 28)
# my_user.display_info()
my_user.enroll()
# my_user.display_info()
my_user.spend_points(50)
# my_user.display_info()

my_user2 = User("Ron", "Swanson", "nothing@nothing.com", 40)
my_user3 = User("Michael", "Scott", "mscott@dundermifflin.com", 42)
# my_user2.display_info()
# my_user3.display_info()

my_user2.spend_points(50) #spending points before enrolling attempt
# my_user2.display_info()
my_user3.enroll()
# my_user3.display_info()
my_user3.spend_points(80)
# my_user3.display_info()

my_user.enroll() #re-enroll attempt
# my_user.display_info()

my_user3.spend_points(200) #overspending attempt
# my_user3.display_info()



