# Begin with total amount of money owed
due = 50

# Loop that runs while money remaining to be deposited is greater than 0
while due > 0:

    # Print amount due and ask user for input
    print("Amount Due:", due)
    coin = input("Insert Coin: ")

    # Continue loop if wrong denomination is entered
    if coin != "5" and coin != "10" and coin != "25":
        continue

    # If correct change is given, apply to total and keep running loop
    due = int(due) - int(coin)

    # Until full amount is paid and loop breaks
    if due <= 0:
        due = abs(due)
        print("Change Owed:", due)
        break
