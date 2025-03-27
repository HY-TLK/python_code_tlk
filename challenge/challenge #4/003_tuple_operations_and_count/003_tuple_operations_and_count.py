#-----------------------------------------------------------------------------
# Name:        003_tuple_operations_and_count
# Purpose:     1. Create a tuple with repeated values.
#              2. Ask the user to enter a fruit name.
#              3. Print how many times that fruit appears in the tuple.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a tuple with repeated values
sample_tuple = ("apple", "banana", "apple", "cherry", "banana", "apple")
print("Original tuple: ", sample_tuple)

# Ask user to enter a fruit name
user_input = input("please enter a fruit name: ")

# Print how many times that fruit appears in the tuple
if user_input in sample_tuple:
    times = sample_tuple.count(user_input.lower())
    print(f"{user_input.lower()} appears {times} times in the tuple.")
else:
    print(f"{user_input.lower()} does not appear in the tuple.")