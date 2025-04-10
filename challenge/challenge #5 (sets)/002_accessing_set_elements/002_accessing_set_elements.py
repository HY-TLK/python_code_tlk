#-----------------------------------------------------------------------------
# Name:        002_accessing_set_elements
# Purpose:     Write a program that uses iteration to access elements in a set.
#
# Author:      Harry Yang
# Created:     06-Apr-2025
#-----------------------------------------------------------------------------

# - Create a set `colors = {'red', 'blue', 'green', 'yellow'}`.
colors = {"red" , "blue" , "green" , "yellow"}
print("the original colors:", colors)
print()

# - Use a loop to print each color in the set.
print("accessing elements with a loop:")
for color in colors:
    print(color)
