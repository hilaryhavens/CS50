from cs50 import get_string

# Assign answer variable to be reply to name query
answer = get_string("What is your name? \n")

# Print answer using format string
print(f"hello, {answer}")