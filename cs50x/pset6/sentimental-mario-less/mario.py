from cs50 import get_int

# While loop to prompt user for integer input that keeps running until integer 1-8 is provided
while True:
    n = get_int("Height: ")
    if n > 0 and n < 9:
        break

# For loop printing n rows of pyramid
for i in range(n):
    print(" " * (n - i - 1) + "#" * (i + 1))