# Ask for the greeting
x = input("Greeting: ").strip().lower()

# If the greeting starts with hello, give no money
if x.startswith("hello") == True:
    print("$0")

# If the greeting starts with hello, give $20
elif x.startswith("h", 0) == True:
    print("$20")

# Otherwise, give $100
else:
    print("$100")