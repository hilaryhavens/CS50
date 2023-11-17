# List of written out months
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

# Prompt user for date
while True:
    date = input("Date: ")

    # Check to see if the date input can be split across "/"
    if len(date.split("/")) == 3:

        # Try number + / split version first
        try:
            x, y, z = date.split("/")

            # Remove whitespace
            x = x.strip()
            y = y.strip()
            z = z.strip()

            # Ensure x and y have valid options and break loop if so
            if 1 <= int(x) <= 12 and 1 <= int(y) <= 31:
                x = ('{:02}'.format(int(x)))
                y = ('{:02}'.format(int(y)))
                print(z + "-" + x + "-" + y)
                break
        except (ValueError):
            pass

    # If number split doesn't work, try word/number split to see if there are three items
    elif date.find(",") > 0 and len(date.replace(",", "").split(" ")) == 3:
        try:
            x, y, z = date.replace(",", "").split(" ")

            # Remove whitespace
            x = x.strip()
            y = y.strip()
            z = z.strip()

            # Convert x to titlecase and see if it is listed in months
            x = x.title()
            if x in months and 1 <= int(y) <= 31:
                x = months.index(x) + 1
                x = ('{:02}'.format(int(x)))
                y = ('{:02}'.format(int(y)))
                print(z + "-" + x + "-" + y)
                break
        except (ValueError):
            pass

    # if input is in wrong format, continue loop
    else:
        continue

