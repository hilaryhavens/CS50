import re
import sys


def main():
    print(count(input("Text: ")))


def count(s):
    # Strip and convert input to lowercase
    s = s.lower().strip()
    
    # Find the number of times that “um” appears in input
    matches = re.findall(r"\bum[,.:;!\?-]|\bum\b", s)

    # Find the number of matches as int and return it
    n = len(matches)
    return n


if __name__ == "__main__":
    main()
