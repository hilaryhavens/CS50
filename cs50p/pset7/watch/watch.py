import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):

    # Strip formatting from s
    s = s.strip()

    # Extracts any YouTube URL from iFrame src
    if matches := re.search(r"^<iframe[ ](?:width=\"(?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9])\"[ ]height=\"(?:[0-9]|[1-9][0-9]|[1-9][0-9][0-9])\"[ ])?src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)\"(?:.+)?><\/iframe>", s, re.IGNORECASE):
        return("https://youtu.be/" + matches.group(1))

    # If the input does not contain any such URL at all, return None.
    else:
        return(None)

if __name__ == "__main__":
    main()