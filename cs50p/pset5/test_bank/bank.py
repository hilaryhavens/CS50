def main():
    # Ask for the greeting
    x = input("Greeting: ")

    # Print the value based on the greeting
    print("$" + value(x))


def value(greeting):

    # Make sure greeting is case insensitive
    greeting = greeting.strip().lower()

    # If the greeting starts with hello, give no money
    if greeting.startswith("hello") == True:
        return 0

    # If the greeting starts with hello, give $20
    elif greeting.startswith("h", 0) == True:
        return 20

    # Otherwise, give $100
    else:
        return 100


if __name__ == "__main__":
    main()
