import random
import sys

# Create a loop that requests an integer input from the user
while True:
    try:
        x = int(input("Level: "))

        # Check for integer at least equal to 1
        if x < 1:
            pass

        # Select a random integer between 1 and x
        n = random.randint(1, x)

        # Create another loop
        while True:
            try:
                y = int(input("Guess: "))

                # Ensure y is not greater than x
                if y > x or y < 1:
                    pass

                # Compare y with n using if/else
                elif y > n:
                    print("Too large!")
                    pass

                elif y < n:
                    print("Too small!")
                    pass

                elif y == n:
                    print("Just right!")
                    sys.exit()

            # Return to guess loop if user doesn't give an integer
            except ValueError:
                pass

    # Return to prompt loop if user doesn't give an integer
    except ValueError:
        pass

