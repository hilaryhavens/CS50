from PIL import Image, ImageOps
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
    if (
        sys.argv[1].lower().split(".")[1] != "jpg"
        and sys.argv[1].lower().split(".")[1] != "jpeg"
        and sys.argv[1].lower().split(".")[1] != "png"
    ):
        print("Invalid input")
        sys.exit(1)
except IndexError:
    print("Invalid input")
    sys.exit(1)

# If input and output have different extensions, exit
if sys.argv[1].lower().split(".")[1] != sys.argv[2].lower().split(".")[1]:
    print("Input and output have different extensions")
    sys.exit(1)

# Open input and shirt files
try:
    with Image.open(sys.argv[1]) as input:
        shirt = Image.open("shirt.png")
        size = shirt.size

        # Resize input to fit shirt size
        new_input = ImageOps.fit(input, size=size)

        # Paste shirt over input file and save it to output file
        new_input.paste(shirt, mask=shirt)
        new_input.save(sys.argv[2])

# Error checking for non-existent files
except FileNotFoundError:
    print(f"Could not read {sys.argv[1]}")
    sys.exit(1)
