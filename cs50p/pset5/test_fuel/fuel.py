import sys

def main():

    # Ask user for fraction input
    fraction = input("Fraction: ")

    # Convert it to a percent
    percent = convert(fraction)

    # Print gauge reading
    print(gauge(percent))


def convert(fraction):
    # Prompts the user for a fraction, formatted as X/Y
    while True:
        try:
            x, y = fraction.split("/")
            # Output, as a percentage rounded to the nearest integer, how much fuel is in the tank.
            level = float(int(x)/int(y))
            percent = round((level * 100))
            # Confirm X is not greater than Y
            if percent <= 100:
                return percent
        # If, though, X or Y is not an integer or Y is 0, instead prompt the user again.
        except (ValueError, ZeroDivisionError) as e:
            sys.exit(1)


def gauge(percentage):
    # If 1% or less remains, output E
    if percentage <= 1:
        return("E")
    # And if 99% or more remains, output F
    elif percentage >= 99:
        return("F")
    # Otherwise, return the actual percent
    else:
        return(f"{percentage}%")



if __name__ == "__main__":
    main()

