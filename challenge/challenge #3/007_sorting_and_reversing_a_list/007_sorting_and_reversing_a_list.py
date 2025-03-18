#-----------------------------------------------------------------------------
# Name:        007_sorting_and_reversing_a_list
# Purpose:     Work with sorting and reversing lists.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list fruits = ['banana', 'apple', 'grape', 'kiwi', 'orange'].
fruits = ["banana","apple","grape","kiwi","orange"]

# Sort the list fruits in alphabetical order (ascending).
# Then, reverse the sorted list to get it in descending order.
# Print both the sorted list and the reversed list.
fruits.sort()
print(fruits)
fruits.sort(reverse=True)
print(fruits)
