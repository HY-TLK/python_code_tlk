#-----------------------------------------------------------------------------
# Name:        002_swapping_values_using_tuples
# Purpose:     Python allows swapping values easily using tuples
#
# Author:      Harry Yang
# Created:     27-Mar-2025
#-----------------------------------------------------------------------------

# Create a function to convert data type from string to integer or float
def convert_numbers(s):
    if "." in s:
        return float(s)
    else:
        return int(s)

# Ask the user to input two numbers
user_input = input("Please enter two numbers separated by a space : ")
# Store them in a tuple
tuple_1 = tuple(convert_numbers(num) for num in user_input.split())
print("Original tuple: " , tuple_1)

# Swaps their values without using a temporary variable.
tuple_1 = tuple_1[1], tuple_1[0]
print("Swapped tuple: " , tuple_1)


