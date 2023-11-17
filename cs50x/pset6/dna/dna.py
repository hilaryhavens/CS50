import csv
import sys


def main():

    # TODO: Check for command-line usage
    if len(sys.argv) != 3:
        sys.exit("Usage: python dna.py data.csv sequence.txt")

    database = []
    # TODO: Read database file into a variable
    # Define variable count to get number of rows in a database
    count = 0
    # Define filename
    filename = sys.argv[1]
    # Open csv file and read those teams into dictionary
    with open(filename) as file:
        # Store each person row as dictionary inside file
        reader = csv.DictReader(file)
        for row in reader:
            database.append(row)
            count += 1
        # Convert dictionary to series of lists
        datalist = []
        for n in range(0, (count - 1)):
            datalist.append(list(database[n].values()))

    # Create a file where the DNA sequence will be stored
    text = []
    # TODO: Read DNA sequence file into a variable
    # Define f as name of text file and open it
    with open(sys.argv[2], "r") as f:
        text = f.read()

    # TODO: Find longest match of each STR in DNA sequence
    # Create a list of the keys from database
    STR = list(database[0].keys())[1:]
    # Define dictionary of matches
    match = {}
    match_cmp = []
    # Record the longest match of the key files at given positions in the same position as keys
    for i in range(0, len(STR)):
        match[i] = longest_match(text, STR[i])
    match_cmp = list(match.values())

    # TODO: Check database for matching profiles
    # Iterate over the rows of the database
    for j in range(0, (count - 1)):
        name = datalist[j][0]
        # Check the DNA values in each column
        for k in range(0, (len(STR) - 1)):
            # Compare the database with the longest matches, iterating through until a match or no match is determined
            while int(match_cmp[k]) == int(datalist[j][k + 1]):
                if k < (len(STR) - 1):
                    k += 1
                elif k == (len(STR) - 1):
                    print(name)
                    sys.exit(0)
                else:
                    break
    print("No match")
    sys.exit(1)


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in sequence, return longest run found
    return longest_run


if __name__ == "__main__":
    main()