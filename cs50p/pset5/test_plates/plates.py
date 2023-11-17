def main():
    # Ask user for input
    plate = input("Plate: ")

    # Run test to see if plate is valid and print result
    if is_valid(plate):
        print("Valid")

    else:
        print("Invalid")


def is_valid(s):
    # vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if len(s) < 2 or len(s) > 6:
        return False

    # All vanity plates must start with at least two letters.
    if not s[0:2].isalpha():
        return False

    # “No periods, spaces, or punctuation marks are allowed.”
    if not s.isalnum():
        return False

    # “Numbers cannot be used in the middle of a plate; they must come at the end.
    for c in s:
        # Find numeric characters
        if c.isnumeric():
            # Find their index
            i = s.index(c)
            # Confirm that no alphabetical characters appear after that point
            if not s[i: len(s)].isdigit():
                return False

            # Confirm that not 0 if it is the first number
            if s[0:(i)].isalpha() and int(c) == 0:
                return False

    else:
        return True


if __name__ == "__main__":
    main()
