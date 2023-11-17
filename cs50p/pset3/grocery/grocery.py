# Create blank dictionary of grocery items and quantity
list = {}

# Create loop that runs until user exits
try:
    while True:
        # Ask user for name of grocery item and change it to upper case
        x = input("").upper()

        # If item is in the menu, find value and add to total
        if x in list:
            list[x] += 1

        # Otherwise, create new dictionary entry
        else:
            list[x] = 1

# Break full list when user presses Ctrl-D
except EOFError:
    for key, value in sorted(list.items()):
        print(value, key)