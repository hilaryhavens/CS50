import csv
import sys

# Error checking
# If wrong number of inputs, exit
if len(sys.argv) < 3:
    print("Too few command-line arguments")
    sys.exit(1)

# If wrong number of inputs, exit
if len(sys.argv) > 3:
    print("Too many command-line arguments")
    sys.exit(1)

# If file has wrong extension, exit
try:
    if (sys.argv[1].split("."))[1] != "csv":
        print("Not a CSV file")
        sys.exit(1)
except IndexError:
    print("Not a CSV file")
    sys.exit(1)

# Create two tables to store data
students = []
table = []

# Open file and write contents to dictionary
try:
    with open(sys.argv[1]) as input:
        reader = csv.DictReader(input)
        for row in reader:
            students.append({"name": row["name"], "house": row["house"]})

# Error checking for non-existent files
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)

# Split student names into new group of dictionaries
for student in students:
    student["last"], student["first"] = student["name"].split(", ")
    table.append(
        {"first": student["first"], "last": student["last"], "house": student["house"]}
    )

# Open output file and define fieldnames
with open(sys.argv[2], "w") as output:
    fieldnames = ["first", "last", "house"]
    writer = csv.DictWriter(output, fieldnames=fieldnames)

    # Iterate over table and put each row into new spreadsheet
    writer.writeheader()
    for item in table:
        writer.writerow(item)
