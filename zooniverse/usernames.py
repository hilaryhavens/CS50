# Code courtesy of Trevor Winger (U Minnesota)

import pandas as pd

import os


# Open classification file (replace "file_name.csv with your particular file name) and select column with contributor names

data = pd.read_csv('file_name.csv')


data.head()


# Exclude contributors who were not logged in

data = data[~data['user_name'].str.contains('not')]


# Print the unique contributor names in the terminal

print(data['user_name'].unique())

# Create a new file named "usernames.txt" to include the text output of the usernames

output = open("usernames.txt", "w")

# Separate names by comma and space and close file

output.writelines(data['user_name'].unique() + ', ')

output.close()


#run sed command to replace _ with \_ in usernames.txt, save as usernames2.txt

os.system("sed 's/_/\\\\_/g' usernames.txt > usernames2.txt")