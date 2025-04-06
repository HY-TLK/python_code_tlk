#-----------------------------------------------------------------------------
# Name:        003_adding_and_removing_elements
# Purpose:     Write a program that uses '.add()', '.remove()', and '.discard()' methods to modify sets.
#
# Author:      Harry Yang
# Created:     06-Apr-2025
#-----------------------------------------------------------------------------

# - Create a set `numbers = {1, 2, 3, 4, 5}`.
numbers = {1,2,3,4,5}
print("original numbers:", numbers)

# - Add `6` and `7` to the set.
numbers.add(6)
numbers.add(7)
print("after adding numbers:", numbers)

# - Remove `2` from the set.
numbers.remove(2)
print("after removing numbers:", numbers)

# - Print the updated set.
print("the final set is:", numbers)