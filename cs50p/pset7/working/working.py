import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    # Strip formatting from s
    s = s.strip()

    # Regex for time input
    matches = re.search(
        r"^([1-9]|[1][0-2])(?:\:([0-5][0-9]))?[ ](?:(A|P)M)[ ]to[ ]([1-9]|[1][0-2])(?:\:([0-5][0-9]))?[ ](?:(A|P)M)$",
        s,
    )

    if matches:
        # Assign group names
        start = matches.group(1)
        s_min = matches.group(2)
        s_time = matches.group(3)
        end = matches.group(4)
        e_min = matches.group(5)
        e_time = matches.group(6)

        # Add 12 to time for PM conversion
        if s_time == "P" and start != "12":
            start = int(start) + 12
        if e_time == "P" and end != "12":
            end = int(end) + 12

        # Edge case for midnight to 0 hours
        if start == "12" and s_time == "A":
            start = 0
        if end == "12" and e_time == "A":
            end = 0

        # Preserve minutes or add extra digits
        if s_min == None:
            s_min = "00"
        if e_min == None:
            e_min = "00"

        # Ensure start and end are converted to int so they can have 2 digits
        start = int(start)
        end = int(end)

        # Return 24 hour time
        return f"{start:02}:{s_min} to {end:02}:{e_min}"

    # Raise a ValueError instead if the input is not in correct format or if either time is invalid
    else:
        raise ValueError("Invalid input")


if __name__ == "__main__":
    main()
