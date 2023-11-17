import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Do a regex search for valid IPv4 address format
    if re.search(
        r"^\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b\.\b([0-9]|[1-9][0-9]|1[0-9][0-9]|2[0-4][0-9]|25[0-5])\b$",
        ip,
    ):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
