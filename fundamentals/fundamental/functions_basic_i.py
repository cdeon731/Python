#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
"""
Prediction: it will print 5
"""


# #2
# def number_of_military_branches():
#     return 5
# print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
"""
Prediction: it will print an error because number_of_days_in_a_week_silicon_or_triangle_sides() 
has not been defined until later on in this assignment after this print statement
"""


#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
"""
Prediction: it will print 5 and 10 will be skipped because a function will only return the first return value then stop
"""


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
"""
Prediction: it will print 5 and skip print(10) because it automatically ignores everything after the return
"""

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
"""
Prediction: it will print 5 and none because its only printing 5 once in the fuction and no longer exists
when called again in x
"""


# #6
# def add(b,c):
#     print(b+c)
# print(add(1,2) + add(2,3))
"""
Prediction: it will print none, then 3 and 5 and then show an error because add(3)+add(5) won't be able to print anything
after the print fuction has already been called, you would need a return statement instead of print in the fuction to add the 3 and 5 together
therefor the computer will read it as nothing + nothing and return: TypeError: unsupported operand type(s) for +:
"""

#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
"""
Prediction: it will print 25 because the function is reading the 2 parameters as strings 
and the arguements "2" and "5" will be added together (concatenated) as such
"""

#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
"""
Prediction: first it will print 100
next 100 is not less than 10 so the if statement gets skipped and the else
statement returns 10
return 7 is skipped because a return has already been called
finally it will print only the first 100 that is equal to b and the 10 that was returned
from the if/else statement
"""


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
"""
Prediction: it will print 7 then 14 then 21
return 3 will be ignored because a return statement will have already been called by that point in the code
"""

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
"""
Prediction: it will print 8 and ignore return 10 for the same reason as the above example
"""

#11
b = 500
print(b)
def foobar():
    b = 300
    print(b)
print(b)
foobar()
print(b)
"""
Prediction: it will first print 500, then it will print 300 inside the foobar function but not until the function is called,
then it will print 500 because b outside of foobar() is still equal to 500, now the 300 will be printed for the foobar() function,
finally 500 will be printed again making the whole print-out look like this:
500
500
300
500
"""

#12
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
foobar()
print(b)
"""
Prediction: it will print:
500
500
300 - it will only print 300 once because although print(b) and return b will give the same result
only the print statements can be seen in the terminal
500
"""

#13
b = 500
print(b)
def foobar():
    b = 300
    print(b)
    return b
print(b)
b=foobar()
print(b)
"""
Prediction: it will print:
500
500
300
300
because after the second 500 is printed the value of b is change to equal the foobar() function and this will print the first 300
then the second 300 prints because b is called again with its new value
"""

#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
"""
Prediction: it will print 1, 3, 2 because foo() is called after both bar() and foo() have been defined
"""

#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
print(y)
"""
Prediction: it will print 1,3,5,10 respectively
"""