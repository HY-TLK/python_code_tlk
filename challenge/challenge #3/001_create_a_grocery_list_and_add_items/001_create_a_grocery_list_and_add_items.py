#-----------------------------------------------------------------------------
# Name:        001_create_a_grocery_list_and_add_items
# Purpose:     Create a list of groceries and then add new items to the list.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list called grocery_list
grocery_list = ["apple","bread","milk","egg"]

# Add two more items to the list: 'cheese' and 'tomatoes'
grocery_list.extend(["cheese","tomatoes"])

# Print the updated list
print(grocery_list)