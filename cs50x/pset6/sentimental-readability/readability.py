from cs50 import get_string

# Ask for text input
text = get_string("Text: ")

# Calculate length
length = len(text)

# Calculate number of letters by counting spaces
letters = 0
for i in range(0, length):
    if text[i].isalpha():
        letters += 1

# Calculate number of words through string split function
words = len(text.split())

# Calculate sentences through if statements for each punctuation type
sentences = 0
for j in range(0, length):
    if text[j] == ".":
        sentences += 1
    elif text[j] == "?":
        sentences += 1
    elif text[j] == "!":
        sentences += 1

# Defines L as average number of letters per 100 words
L = (letters / words) * 100

# Defines S as average number of sentences per 100 words
S = (sentences / words) * 100

# Place variables in formula
index = (0.0588 * L) - (0.296 * S) - 15.8

# Round number to nearest integer
level = round(index)

# Execute a series of "if" statements to check actual level
# If reading level is below grade 1
if level < 1:
    print("Before Grade 1")

# If reading level is at least grade 1 and less than grade 16
if level >= 1 and level < 16:
    print(f"Grade {level}")

# If reading level is above grade 16
if level > 16:
    print("Grade 16+")

