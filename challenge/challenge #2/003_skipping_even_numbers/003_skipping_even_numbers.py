#-----------------------------------------------------------------------------
# Name:        Skipping even numbers - For (003_skipping_even_numbers.py)
# Purpose:     Write a program that prints numbers from 1 to 10, but skips even numbers
#
# Author:      Harry Yang
# Created:     04-Mar-2025
#-----------------------------------------------------------------------------

# Use a for loop to iterate over the integers from 1 to 10 (inclusive)
for i in range (1,11):
    # Use the conditional statement to check whether the number is an even number
    if i % 2 == 0:
        # If it's an even number, Skip the remainder of the current loop and continue with the next loop
        continue
    # If it is not an even number (i.e. an odd number), print the current number
    print(i)