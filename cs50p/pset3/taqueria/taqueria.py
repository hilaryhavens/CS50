# Define dictionary of menu items and cost
menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

# Initialize total to 0
total = 0

# Create loop that runs until user exits
try:
    while True:
        # Ask user for name of menu item and change it to title case
        x = input("Item: ").title()

        # If item is in the menu, find value and add to total
        if x in menu:
            cost = menu[x]
            total = cost + total

        # Print total
        print("Total: $", end='')
        print("%.2f" % total)

# Break when user presses Ctrl-D
except EOFError:
    print("")