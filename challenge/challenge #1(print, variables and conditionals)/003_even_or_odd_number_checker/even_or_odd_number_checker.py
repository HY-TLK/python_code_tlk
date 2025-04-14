#-------------------------------------------------------------------------
# Name:         Odd or Even number Checker (odd_or_even_number_checker.py)
# Purpose:      To create a checker for numbers
#
# Author:       Harry Yang
# Created:      24-Feb-2025
#-------------------------------------------------------------------------

# Ask the user to enter a number
# Store the number in a variable
number_input = int(input("please enter a number: "))


# Use conditional statements to check if the number is even or odd.

# Even number
if number_input % 2 == 0:
    print(f"{number_input} is an even number.")

# Odd number
elif number_input % 2 != 0:
    print(f"{number_input} is an odd number.")
