num1 = 42
#variable declaration/ number/ interger

num2 = 2.3
#variable declaration/ number/ float

boolean = True
#data type/ primitive/ boolean

string = 'Hello World'
#data type/ primitive/ string

pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
#data type/ composite/ list

person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
#data type/ composite/ dicitonary

fruit = ('blueberry', 'strawberry', 'banana')
#data type/ composite/ tuples

print(type(fruit))
#data type/ composite/ tuples/ initialize

print(pizza_toppings[1])
#data type/ composite/ list/ access value/ 'Sausage'

pizza_toppings.append('Mushrooms')
#data type/ composite/ list/ add value

print(person['name'])
#data type/ composite/ dictionary/ access value

person['name'] = 'George'
#data type/ composite/ dictionary/ change value

person['eye_color'] = 'blue'
#data type/ composite/ dictionary/ add value

print(fruit[2])
#data type/ composite/ list/ access value/ 'banana'

if num1 > 45:
    print("It's greater")
else:
    print("It's lower")
#conditional/ if else

if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!")
else:
    print("Just right!")
#conditional/ if elseif else

for x in range(5):
    print(x)
for x in range(2,5):
    print(x)
for x in range(2,10,3):
    print(x)
x = 0
while(x < 5):
    print(x)
    x += 1
#for loop/ while loop

pizza_toppings.pop()
#remove last topping from list
pizza_toppings.pop(1)
#remove specific topping from list

print(person)
person.pop('eye_color')
print(person)
#remove eye color value from list

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue
    print('After 1st if statement')
    if topping == 'Olives':
        break
#for loop continue/ for loop break

def print_hello_ten_times():
    for num in range(10):
        print('Hello')
#function/ parameter/ for loop

print_hello_ten_times()
#function/ return

def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#function/ argument/ parameter/ for loop

print_hello_x_times(4)
#function/ return 4x's

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')
#function/ parameter/ for loop 10x's

print_hello_x_or_ten_times()
#function/ return
print_hello_x_or_ten_times(4)
#function/ return x=10 function 4x's



"""
Bonus section
"""

#print(num3)
#- NameError: name <num3> is not defined

#num3 = 72
#variable declaration/ number/ interger

#fruit[0] = 'cranberry'
#- TypeError: 'tuple' object does not support item assignment/ tuples are immutable(can't be changed)

#print(person['favorite_team'])
#- KeyError: 'favorite_team'/ 'favorite team' doesn't exist

#print(pizza_toppings[7])
#- IndexError: list index out of range/ there aren't 8 toppings in dictionary

#   print(boolean)
#- IndentationError: unexpected indent

# fruit.append('raspberry')
#- AttributeError: 'tuple' object has no attribute 'append'/ tuples are immutable

# fruit.pop(1)
#- AttributeError: 'tuple' object has no attribute 'pop'/ tuples are immutable