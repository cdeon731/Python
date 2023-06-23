class Ninja:
    def __init__(self, first_name , last_name , treats , pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    
    def __repr__(self):
        display = f"Name: {self.first_name} {self.last_name}, Treats: {self.treats}, Pet Food: {self.pet_food}, Pet: {self.pet}"
        return display

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()
        return self

    def bathe(self):
        self.pet.pet_noise()

class Pet:
    def __init__(self, name , type , tricks, noise):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 100
        self.energy = 100
        self.noise = noise
    
    def __repr__(self):
        display = f"Name: {self.name}, Type: {self.type}, Tricks: {self.tricks}, Noise: {self.noise}"
        return display

    def sleep(self):
        self.energy += 25
        return self
    
    def eat(self):
        self.energy += 5
        self.health +=10
        return self

    def play(self):
        self.health += 5
        return self

    def pet_noise(self):
        print(self.noise)

dog = Pet("Silas", "Australian Cattle", "sit, stay, lie down", "woof!")

ninja = Ninja("Casey", "D'Eon", "dog-treat", "chicken", dog)
print(ninja)

ninja.feed()
ninja.walk()
print(dog.health)
print(dog.energy)

ninja.bathe()