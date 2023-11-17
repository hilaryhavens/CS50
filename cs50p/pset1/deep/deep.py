# Ask user for the great answer
answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

# If condition for correct answer of 42
if answer.lower() == "forty two" or answer.lower() == "forty-two" or answer.strip() == "42":
    print("Yes")

# Negative for everything else
else:
    print("No")