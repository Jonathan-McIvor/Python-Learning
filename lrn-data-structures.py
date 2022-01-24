# Data structures with respective characters in front of them below:
    # list : []
    # tuple : ()
    # dictionary : {}

# List() function which has a very simple implementation and usage
mylist = ["ski boots", "skis", "gloves"]
print(mylist)
print(type(mylist))

mylist = ["carabiners", False, "chalk powder", 666, 25.25]
print(mylist)
print(type(mylist))

# Dict() function which helps you create a Python dictionary
mydict = {"ski boots": 3, "skis": 2, "gloves": 5}
print(mydict)
print(type(mydict))

# Tuple() function which helps you create a Python tuple
mytuple = ("carabiners", False, "chalk powder", 666, 25.25)
print(mytuple)
print(type(mytuple))


# Strings:
    #.lower()
    #.upper()
    #.capitalize()
    #.startswith()
    #.endswith()
    #.join()
    #.split()
    #.strip()
    #.index()
    #.count()
    #.find()
    #.min()
    #.max()
    #.replace()
    #len()
    #type()

# Lists:
    #.append()
    #.insert()
    #.pop()
    #.remove()
    #.replace()
    #.index()
    #.count()
    #.sum()
    #.reverse()
    #.clear()
    #.min()
    #.max()
    #len()

# Dictionaries:
    #.clear()
    #.copy()
    #.keys()
    #.items()
    #.get()
    #len()
    #type()

# Tuples:
    #.count()
    #.sum()
    #.min()
    #.max()
    #len()
    #type()

# Items  in string format can be confusing and hard to read in this format
lst = ['Unnamed: 0', 'id', 'date', 'price', 'bedrooms', 'bathrooms', 
'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 
'year_built', 'year_renovated', 'zipcode']
print(lst)

# Here is a simple for loop which will print lists vertically
lst = ['Unnamed: 0', 'id', 'date', 'price', 'bedrooms', 'bathrooms', 
'sqft_living', 'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 
'year_built', 'year_renovated', 'zipcode']
for i in lst:
    print(i)

# Can also use ' print(*lst, sep="\n") ' 


# Enumerate function and vertical printing all in just one line.
# Enumerate function can be used to give numbers to each list item or “enumerate” it

lst = ["libor", "gold", "treasury_bond", "stock_options"]
print(enumerate(*lst, 100), sep="\n")

# Normally  enumerate function starts counting from 0 by default, 
# - so we are also passing a value to its second parameter so it starts counting from 100
