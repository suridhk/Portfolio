'''
15. Write a program to create a number guessing game for the user. The program should ask
the user to input a number. The program specifications are as mentioned below.
I. The program should generate a random number for the answer.
II. The program should prompt the user for a number input.
III. The program should provide the feedback to the user after each guesses (e.g. “Too
high”, “Too low” or “Correct number”).
IV. The program should check the user input for 5 times and allow the users to guess for
at most 5 times if their input don’t match the answer number.
V. If the user is not able to guess the answer within 5 times, the program should display
“Game Over” message and exit.
'''

import random

# Generate a random number between 1 and 100
secret = random.randint(1, 100)

# Allow the user to guess up to 5 times
for i in range(5):
    guess = int(input("Guess a number: "))

    if guess > secret:
        print("Too high")
    elif guess < secret:
        print("Too low")
    else:
        # Correct guess
        print("Correct number! You won!")
        break  # Exit the loop if guessed correctly
else:
    # Executed if the loop finishes without a correct guess
    print("Game Over! The number was", secret)
