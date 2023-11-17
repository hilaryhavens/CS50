# Import necessary libraries
from pyfiglet import Figlet
import sys
import random

# Create shorthand for referring to Figlet library
figlet = Figlet()

# Check for errors
# Too many arguments
if len(sys.argv) > 3 or len(sys.argv) == 2:
    sys.exit("Invalid usage")

# Incorrect font signalling
if len(sys.argv) == 3 and sys.argv[1] != "-f" and sys.argv[1] != "--font":
    sys.exit("Invalid usage")

# Incorrect font name
list = figlet.getFonts()
if len(sys.argv) == 3 and sys.argv[2] not in list:
    sys.exit("Invalid usage")

# Prompts the user for a str of text.
text = input("Input: ")

# Outputs that text in the desired font.
if len(sys.argv) == 3:
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(text))

# Or outputs text in random font by randomizing entry in list
else:
    n = len(list)
    rfont = random.randint(0, (n - 1))
    rname = list[rfont]
    figlet.setFont(font=rname)
    print(figlet.renderText(text))