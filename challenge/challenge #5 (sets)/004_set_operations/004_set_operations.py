#-----------------------------------------------------------------------------
# Name:        004_set_operations
# Purpose:     Write a program to combine and compare sets using set operations.
#
# Author:      Harry Yang
# Created:     06-Apr-2025
#-----------------------------------------------------------------------------

# - Create two sets: `set1 = {1, 2, 3, 4}` and `set2 = {3, 4, 5, 6}`.
set1 = {1,2,3,4}
set2 = {3,4,5,6}
print("set1:", set1)
print("set2:", set2)

# - Print the union, intersection, and difference.
print("the union set: ", set1 | set2)
print("the intersection set: ", set1 & set2)
print("the difference:", set1 - set2)