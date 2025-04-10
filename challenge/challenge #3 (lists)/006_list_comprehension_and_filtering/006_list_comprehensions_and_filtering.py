#-----------------------------------------------------------------------------
# Name:        006_list_comprehensions_and_filtering
# Purpose:     Use list comprehensions to filter and manipulate data based on a condition.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].
print("here is a list of numbers")
nums = [1,2,3,4,5,6,7,8,9,10]
print(nums)

# Using a list comprehension, create a new list even_numbers that contains only the even numbers from the numbers list.
even_nums = [i for i in nums if i % 2 == 0]

# Then, create a list squared_numbers that contains the squares of all the even numbers from the even_numbers list.
squared_nums = [i**2 for i in nums if i % 2 == 0]

# Print both the even_numbers and squared_numbers lists.
print("Even numbers: ",even_nums)
print("Squared numbers: ",squared_nums)
