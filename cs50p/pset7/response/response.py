from validator_collection import checkers

# Prompt the user for an email address via input
email = input("What's your email address? ")

# Print Valid or Invalid if the input is a syntatically valid email address
if checkers.is_email(email) is True:
    print("Valid")
else:
    print("Invalid")

