# 1. Countdown
def countdown(a):
    countdown_list = []
    for i in range(a,-1,-1):
        countdown_list.append(i)
        print(countdown_list)

countdown(5)

# 2. Print and Return
def print_and_return(x):
    print(x[0])
    return x[1]

print_and_return([3,6])

# 3. First Plus Length
def first_length(a):
    x = a[0] + len(a)
    print(x)

first_length([2,4,5,8])

# 4. Values Greater than Second
def greater_than_second(a):
    x = []
    if len(a) < 2:
        return False
    for i in range(0,len(a)):
        if a[i] > a[1]:
            x.append(a[i])
    print(len(x))
    return x
print (greater_than_second([5,4,32,2,15,0,8,1]))
print (greater_than_second([3]))

# 5. This Lenght, That Value
def length_value(size, value):
    x = []
    for i in range(0, size):
        x.append(value)
    print (x)

length_value(12,34)
length_value(16,2)
