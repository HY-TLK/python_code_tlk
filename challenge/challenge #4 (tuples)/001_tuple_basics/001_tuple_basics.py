#-----------------------------------------------------------------------------
# Name:    001_tuple_basics
# Purpose: Create a tuple with five different elements,
#          including an integer, a float, a string, a boolean, and another tuple.
#          Then, write code to:
#          1. Print the entire tuple.
#          2. Access and print the third element.
#          3. Extract the nested tuple and print its first element.
#
# Author:      Harry Yang
# Created:     27-Mar-2025
#-----------------------------------------------------------------------------

# Create a tuple with five different elements, including an integer, a float, a boolean, and another tuple
sample_tuple = (1 , 2.3 , "harry" , True , (7,8,9))
print(sample_tuple ,"\ntuple is created")

# Print the entire tuple
print("the entire tuple is: " , sample_tuple)
# Access and print the third elements
print("the third element is: " , sample_tuple[2])
# Extract the nested tuple and print its first element
print("the nested tuple is: " , sample_tuple[4])
print("the first element is: " , sample_tuple[4][0])