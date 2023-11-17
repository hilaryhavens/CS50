import sys

# Error checking
# If wrong number of inputs, exit
if len(sys.argv) < 2:
    print("Too few command-line arguments")
    sys.exit(1)

# If wrong number of inputs, exit
if len(sys.argv) > 2:
    print("Too many command-line arguments")
    sys.exit(1)

# If file has wrong extension
if (sys.argv[1].split("."))[1] != "py":
    print("Not a Python file")
    sys.exit(1)


# Create a variable to store number of lines
lines = 0

# Open file and check for number of lines
try:
    with open(sys.argv[1], "r") as file:
        for line in file:
            # Remove comments and blank lines from consideration
            if line.lstrip().startswith("#") or line.lstrip() == "":
                lines = lines

            else:
                lines += 1

# Error checking for non-existent files
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

print(lines)
