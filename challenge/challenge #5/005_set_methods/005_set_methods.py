#-----------------------------------------------------------------------------
# Name:        005_set_methods
# Purpose:     Write a program to demonstrate various set methods.
#
# Author:      Harry Yang
# Created:     04-Mar-2025
#-----------------------------------------------------------------------------

# - Create a set `data = {10, 20, 30, 40, 50}`.
data = {10,20,30,40,50}
print("data : " , data)

# - Copy the set to `data_copy` and print it.
data_copy = data.copy()
print("data_copy : " , data_copy)

# - Use `.pop()` to remove a random element and print the set.
data.pop()
print("after removing a random element , data : " , data)

# - Use `.clear()` to empty the set and print it.
data.clear()
print("after empty the set , data : " , data)