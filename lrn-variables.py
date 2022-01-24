# A variable is a “named container” of data you’d like to refer to in your program

# You can start a variable name with a letter or underscore
variable1 = "Test"

# If you want to print a variable this will have to be without quotes
print(variable1)

# Let’s say you have a big number you’re working with at hand: 
# 149,597,870. This number denotes the average distance between sun and our planet earth in kilometers.
sun_to_earth=149597870
sun_to_earth=sun_to_earth+402130
print(sun_to_earth)

# some names are reserved in Python so you can not use these such as:
# - print, true, false, count, sum etc.

# Variable names have to start with a letter or underscore(_)
# You can include numbers, if you started your variable name correctly with a letter or underscore.

# Variable name is case sensitive

dogsName = "Oscar"
dogsKind = "Doberman"
print("His name is",dogsName,".","He is a",dogsKind,".")

# You can also assign multiple variables in one line in Python
i,j,k = "Hello",55,21.0765
print(i,j,k)
