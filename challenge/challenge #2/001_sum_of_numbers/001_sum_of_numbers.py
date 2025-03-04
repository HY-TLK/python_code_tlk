#-----------------------------------------------------------------------------
# Name:        001_sum_of_numbers - For (001_sum_of_numbers.py)
# Purpose:     Write a program that asks the user for a number `n`
#              and calculates the sum of all numbers from `1` to `n` using a `for` loop.
#
# Author:      Harry Yang
# Created:     04-Mar-2025
#-----------------------------------------------------------------------------

# Ask the user to enter a positive integer
# Store the positive integer in a variable
user_input = int(input("please enter a positive integer: "))

# Create an empty list
sum_list = []

# Use a for loop to iterate over all integers from 1 to (user_input + 1)
for i in range (1,user_input+1):
    # Add every of them into the empty list
    sum_list.append(i)

# Get the sum of all the elements in the list
print(sum(sum_list))