from tabulate import tabulate
import csv
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
try:
    if (sys.argv[1].split("."))[1] != "csv":
        print("Not a CSV file")
        sys.exit(1)
except IndexError:
    print("Not a CSV file")
    sys.exit(1)

# Create table to store data
table = []

# Open file and add each row to the table
try:
    with open(sys.argv[1]) as file:
        reader = csv.DictReader(file)
        for row in reader:
            table.append(row)

# Error checking for non-existent files
except FileNotFoundError:
    print("File does not exist")
    sys.exit(1)

# Print table using tabulate
print(tabulate(table, headers="keys", tablefmt="grid"))
