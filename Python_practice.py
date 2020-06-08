print('hellow orld')
print(type((12,12)))
counties_dict = {}
counties_dict["Arapahoe"] = 422829
counties_dict["Denver"] = 463353
counties_dict["Jefferson"] = 432438

print(counties_dict)
print(counties_dict)

msg = "Hello World"
print(msg)

print(counties_dict)
tuple = (1,2)
print(type(tuple))
list = [1,2]
print(type(list))
dict = {}
dict["Arapahoe"] = 12345
print(dict)

import sys

print(sys.version)
print(sys.executable)

# Integers are positive or negative whole numbers limited only by the amount of RAM in your computer
int = -1200000000

print(type(int))

# Floats are decimals

type(73.81)
print(type(73.81))

# Don't use comma separators in python
ballots = 1, 341
print(type(ballots))

# Strings are text or numbers wrapped by either single or double quotes

print(type('Hellow orld'))

#Booleans are True or False statements, in Python it's always capitalized

is_male = True

print(type(is_male))

#Using len function to get the number of items in dictionary
print(len(counties_dict))

#Is there a .len method? The answer is NO
#print(counties_dict.len)

#Using .items method to get the dictionary items
print(counties_dict.items())

#Using .keys method to get the keys
print(counties_dict.keys())

#Using .get method to get the number of voters for Denver
print(counties_dict.get("Denver"))

# Using .get method to get the number of voters
print(counties_dict.get("Arapahoe"))

# Alternate method to get the number of voters for Arapahoe
print(counties_dict['Arapahoe'])

voting_data = []

voting_data.append({"county":"Arapahoe", "registered_voters": 422829})
voting_data.append({"county":"Denver", "registered_voters": 463353})
voting_data.append({"county":"Jefferson", "registered_voters": 432438})

print(voting_data)

print(len(voting_data))

# .insert method takes two arguments, 1) the index number and 2) the item
voting_data.insert(2, {"county":"El Paso","registered_voters":461149})

# .remove method removes an item
voting_data.remove({"county":"Arapahoe", "registered_voters": 422829})

voting_data.remove({"county":"Denver", "registered_voters": 463353})

voting_data.insert(3, {"county":"Denver", "registered_voters": 463353})

# .append adds an item at the end of the list/dictionary doesn't work for tuples because tuples are immutable
voting_data.append({"county":"Arapahoe", "registered_voters": 422829})

print(voting_data)

# using the len() function
print(len(voting_data))

counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}
for county, voters in counties_dict.items():
    print(county + " county has " + str(voters) + " registered voters.")
    dir(int)
    dir(float)
    dir(bool)