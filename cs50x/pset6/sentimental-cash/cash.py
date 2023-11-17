from cs50 import get_float

# Set counter to 0
counter = 0

# Ask for cents and check for non-negative value
while True:
    cents = get_float("Change owed: ")
    if cents >= 0:
        break

# multiply by 100 to avoid floating point problem
cents = round(cents * 100)

# While loop to iterate through various types of coins
while cents > 0:

    # Check number of quarters and add to counter
    if cents >= 25:
        cents = cents - 25
        counter += 1

    # Check number of dimes and add to counter
    elif cents >= 10:
        cents = cents - 10
        counter += 1

    # Check number of nickels and add to counter
    elif cents >= 5:
        cents = cents - 5
        counter += 1

    # Check number of pennies and add to counter
    elif cents >= 1:
        cents = cents - 1
        counter += 1

# Print counter (coin total)
print(counter)
