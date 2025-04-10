#-----------------------------------------------------------------------------
# Name:        002_access_and_modify_list_items
# Purpose:     Modify a grocery list by changing an existing item.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Start with the list: grocery_list
grocery_list = ["apples","bananas","carrots","milk","bread"]
print(grocery_list)

# Change 'bananas' to 'grapes'.
print("We are going to change bananas to grapes")
grocery_list[1] = "grapes"

# Print the updated list
print(grocery_list)

# Access the third item in the list and print it
print("the third item is",grocery_list[2])