#-----------------------------------------------------------------------------
# Name:        002_guess_a_number (002_guess_a_number.py)
# Purpose:     Write a program that generates a random number between `1` and `10` .
#
# Author:      Harry Yang
# Created:     04-Mar-2025
#-----------------------------------------------------------------------------


# Welcome
print("Welcome to the guessing number game")
print()

# Import the random module
import random

# Get all integers from one to ten
number = random.randint(1,10)

# Create a variable to record how many tries
attempt = 0

# Create a loop so that we can keep asking the user to guess it until they guess correctly
while True:

    # Ask the user to enter a positive integer
    # Store the positive integer in a variable
    user_input = int(input("please enter a positive integer between 1 and 10: "))

    # Use the conditional statement to check if the user get the right answer
    # Get the correct answer
    if user_input == number:
        attempt += 1
        print("The number is ", number)
        print(f"After {attempt} tries! Correct!")
        break
    # Out of range
    if user_input > 10 or user_input < 1:
        print("Out of range")
    # Get the incorrect answer
    else:
        print("Wrong! Try again.")
        attempt += 1