import random


def main():
    # Get level using function
    level = get_level()

    # Set counter to 0
    count = 0

    # Set correct number to 0
    correct = 0

    # Create a loop that terminates at 10
    for count in range(0, 10):

        # Generate the two integers in the addition problem
        a = generate_integer(level)
        b = generate_integer(level)

        # Set error count to 0
        error = 0

        # Loop question until correct answer or maximum
        while True:
            # Break out of question loop if there are three mistakes
            if error == 3:
                print(f"{a} + {b} = {a + b}")
                break

            # Ask user for solution of given problem
            try:
                c = input(f"{a} + {b} = ")

            # Check for value error
            except ValueError:
                print("EEE")
                error += 1
                print(error)

            # If numeric answer
            else:
                # If first answer is correct, break loop
                if int(c) == int(a + b) and error == 0:
                    correct += 1
                    break

                # If subsequent answer is correct, break loop
                elif int(c) == int(a + b) and error > 0:
                    break

            # If answer is incorrect
                else:
                    print("EEE")
                    error += 1

            # Increase count by one after going through loop
            count += 1

    # Once loop is done, print number of correct answers
    print(f"Score: {correct}")


# Function to check that level input is correct
def get_level():
    # Loop asking for level input
    while True:
        try:
            level = int(input("Level: "))

            # Check that input is an integer
            if isinstance(level, int) == False:
                pass

            # Return value if input between 1 and 3
            elif 1 <= int(level) <= 3:
                return level

        # Return to prompt loop if user doesn't give an integer
        except ValueError:
            pass


# Function that randomly generates and returns integers with "i" number of digits
def generate_integer(i):
    if i == 1:
        n = int(random.randint(0, 9))
    else:
        n = int(random.randint(10 ** (i-1), (10 ** i - 1)))
    return n


# Run main function
if __name__ == "__main__":
    main()