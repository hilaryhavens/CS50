# Define main function to get percent
def main():
    p = get_percent()
    # If 1% or less remains, output E
    if p <= 1:
        print("E")
    # And if 99% or more remains, output F
    elif p >= 99:
        print("F")
    # Otherwise, print the actual percent
    else:
        print(f"{p}%")


def get_percent():
    # Prompts the user for a fraction, formatted as X/Y
    while True:
        try:
            x, y = input("Fraction: ").split("/")
            # Output, as a percentage rounded to the nearest integer, how much fuel is in the tank.
            level = float(int(x)/int(y))
            percent = round((level * 100))
            # Confirm X is not greater than Y
            if percent <= 100:
                return percent
        # If, though, X or Y is not an integer or Y is 0, instead prompt the user again.
        except (ValueError, ZeroDivisionError):
            pass


main()