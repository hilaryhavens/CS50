from datetime import date, timedelta, datetime
import sys
import inflect

p = inflect.engine()


def main():
    # Get input from user
    birthday = check_birthday(input("Date of Birth: "))
    # Get difference in days between today and birthday
    days = get_days(birthday)
    # Convert days to total minutes, put in words, and remove "and"
    minutes = p.number_to_words(1440 * days).capitalize().replace(" and ", " ")
    # Print words
    print(f"{minutes} minutes")


def check_birthday(bday):

    # Error checking by converting birthday from isoformat
    try:
        birthday = date.fromisoformat(bday)
        return birthday

    # Exit via sys.exit if the user does not input a date in YYYY-MM-DD format.
    except ValueError:
        print("Invalid date")
        sys.exit(1)


def get_days(birthday):

    # Get today's date
    today = date.today()

    # Get the difference between today and birthday and return number of days
    time = today - birthday
    time2 = time.days
    return time2


if __name__ == "__main__":
    main()
