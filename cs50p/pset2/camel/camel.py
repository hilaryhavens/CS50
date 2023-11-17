# Ask for camel case input
camel = input("camelCase: ")

# Define snake variable
snake = ""

# Loop to check for upper case vs. lower case, iterating over each element
for s in camel:
    if s.isupper():
        snake = snake + "_" + s.lower()
    else:
        snake = snake + s
print("snake_case:", snake)