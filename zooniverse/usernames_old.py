 # Many thanks to Trevor Winger for his help on this code

import pandas as pd
import re

# Open classification file and select column with contributor names
data = pd.read_csv('classifications10142022.csv', usecols= ['user_name'])

data.head()

data = data[~data['user_name'].str.contains('not')]

data['user_name'] = data['user_name'].str.replace('_', r"\ _")
data['user_name'] = data['user_name'].str.replace(' ', '')

print(data['user_name'].unique())

output = open("usernames.txt", "w")

output.writelines(data['user_name'].unique() + ', ')