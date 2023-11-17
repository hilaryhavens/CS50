# Ask for input
text = input("Input: ")

# Create a list of vowels that should be omitted
vowels = ["a", "e", "i", "o", "u"]

# Initialize output
newText = ""

# For loop that iterates through each character
for c in text:

    # If vowel, delete character
    if c.lower() in vowels:
        newText = newText

    # Otherwise, print character
    else:
        newText = newText + c

# Print output
print("Output:", newText)