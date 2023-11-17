import inflect

p = inflect.engine()

# Create empty list to add names
names = []

# Create loop that runs until user exits
try:
    while True:
        # Ask user for name input
        x = input("Name: ")

        # Add name to list
        names.append(x)

# Break when user presses Ctrl-D
except EOFError:
    print("Adieu, adieu, to", p.join(names)) 