x = 0
while x <= 5:
    print(x)
    x = x + 1
#putting a space
print("")
numbers = [0, 1, 2, 3, 4]
for num in numbers:
    print(num)

counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for counties in counties_dict.keys():
    print (counties)
print("")
for voters in counties_dict.values():
    print (voters)
print("")
## use dictionary_name[key] to get the value of the key
print(counties_dict['Arapahoe'])
print("")
##For loops to return a specific key
for county in counties_dict:
    print(counties_dict[county])
print("")
##Alternate Method using the get() method
for county in counties_dict:
    print(counties_dict.get(county))
print("")    
##Getting the key-value pairs of a dictionary, using the .item() method
for county, voters in counties_dict.items():
    print(str(county) +" " +"county has"+" ", str(voters) + " " +"registered voters.")
print("")    
#When iterating over a dictionary:
#The first variable declared in the for loop is assigned to the keys.
#The second variable is assigned to the values.
voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
                {"county":"Denver", "registered_voters": 463353},
                {"county":"Jefferson", "registered_voters": 432438}]

for county in voting_data:
    print(county)

for i in range(len(voting_data)):
    print(voting_data(i))

print("") 
for county_dict in voting_data:
    for value in county_dict.values():
        print(county_dict['registered_voters'])


