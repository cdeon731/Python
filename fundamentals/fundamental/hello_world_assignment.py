# 1. TASK: print "Hello World"
print( "Hello World" )
# 2. print "Hello Casey!" with the name in a variable
name = "Casey"
print( f"Hello, {name}!" )	# with a comma
print( "Hello " + name + "!")	# with a +
# 3. print "Hello 42!" with the number in a variable
fav_number = 7
print( f"Hello, {fav_number}!")	# with a comma
print( "Hello " + str(fav_number) + "!")	# with a +	-- this one should give us an error!
# 4. print "I love to eat sushi and pizza." with the foods in variables
fave_food1 = "pasta"
fave_food2 = "pizza"
print("I love to eat {} and {}.".format(fave_food1, fave_food2)) # with .format()
print(f"I love to eat {fave_food1} and {fave_food2}.") # with an f string

