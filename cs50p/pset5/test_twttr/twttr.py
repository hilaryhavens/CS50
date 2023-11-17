def main():

    # Ask for input
    word = input("Input: ")

    # Print output after running shorten function
    print("Output:", shorten(word))


def shorten(word):

    # Create a list of vowels that should be omitted
    vowels = ["a", "e", "i", "o", "u"]

    # Initialize output
    newWord = ""

    # For loop that iterates through each character
    for c in word:

        # If vowel, delete character
        if c.lower() in vowels:
            newWord = newWord

        # Otherwise, print character
        else:
            newWord = newWord + c

    # Return new word to main function
    return(newWord)


if __name__ == "__main__":
    main()

