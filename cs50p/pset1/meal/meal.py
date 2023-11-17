def main():
    # Ask for input
    time = input("What time is it? ")

    # If between 7:00 and 8:00
    if convert(time) >= 7 and convert(time) <= 8:
        print("breakfast time")

    # If between 12:00 and 13:00
    if convert(time) >= 12 and convert(time) <= 13:
        print("lunch time")

    # If between 18:00 and 19:00
    if convert(time) >= 18 and convert(time) <= 19:
        print("dinner time")


def convert(time):
    # Take into account AM / PM
    if "a.m" in time:
        time = time.replace(" a.m.", "")

    elif "p.m" in time:
        time = time.replace(" p.m.", "")
        hours, minutes = time.split(":")
        # Convert to integers and return value
        new = float(hours) + (float(minutes) / 60) + 12
        return (new)

    # Split out hours and minutes
    hours, minutes = time.split(":")
    # Convert to integers and return value
    new = float(hours) + (float(minutes) / 60)
    return (new)


if __name__ == "__main__":
    main()