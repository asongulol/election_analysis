# The data we need to retrieve
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

#Import the datetime class from the datetime module
import datetime as dt

#Use the now() attribute on the datetime class to get the present time
now = dt.datetime.now()

#Print the present time
print("The time right now is", now)

import csv
import os

#Assign a variable for the file to load and the path
file_to_load = 'Resources/election_results.csv'

#Open the election results and read the file
#election_data = open(file_to_load,'r')

#Open the file using the with statement
with open(file_to_load) as election_data:
    
#To do: perform analysis
    print(election_data)

#Close the file.
#election_data.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

#Write title and three counties to the file
    txt_file.write("\nCounties in the Election")
    txt_file.write('\n-------------------------')
    txt_file.write("\nArapahoe\nDenver\nJefferson")

# Close the file
    txt_file.close()

