# The basic and most common data types in Python are:
    # int : this type of data consists of numbers and particularly integers.
    # float : this type of data refers to numbers with decimals
    # str : standing for string, an str type of variable keeps data as a text string.
    # bool type : consists of only two values: True or False
        # int is used where numbers are needed to be stored
        # float is used when decimals are needed
        # str stores data in a string format and can include any letters, symbols or numbers

myCars_number = 3
myCars_colors = ("Vermont Bronze", "Deep Forest Green", "Graphite Black")
print (myCars_number)
print (myCars_colors)

# use cntrl + shift + L to reassign variable names

# This is a float as it contains numbers after decimal
Glasgow_temp_today = 12.054
print(Glasgow_temp_today)

# This is a int as it contains no numbers after decimal
Glasgow_temp_today = 12
print(Glasgow_temp_today)

# You can also use 'type' function when you aren’t sure of a data’s data type. It will return a string specifying data type accordingly
Glasgow_temp_today = "12.054"
print(type(Glasgow_temp_today))

# This is a boolean as it only returns True or False
hungry_or_not = True
print(hungry_or_not)

# You can do math operations on bool type data. 
# True will be treated as 1 and False as 0. 
# This is accurate with the bit representation on very low level programming which deals with computer on the hardware level.

# Imagine if you have two switches going to the same lightbulb. if one is off it won’t turn on.

switch1 = True
switch2 = False
print(switch1 * switch2)

 