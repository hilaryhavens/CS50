# Ask for user input
expression = input("Expression: ")

# Split out numbers and operator
x, y, z = expression.split(" ")

# Convert number input to floats
x = float(x)
z = float(z)

# If statements for various operations
# Addition
if y == "+":
    print(round(x + z, 1))

# Subtraction
elif y == "-":
    print(round(x - z, 1))

# Multiplication
elif y == "*":
    print(round(x * z, 1))

# Division
elif y == "/":
    print(round(x / z, 1))