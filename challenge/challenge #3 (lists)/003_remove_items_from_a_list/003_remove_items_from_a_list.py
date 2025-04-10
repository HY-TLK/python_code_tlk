#-----------------------------------------------------------------------------
# Name:        003_remove_items_from_a_list
# Purpose:     Remove an item from a list.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list todo_list
todo_list = ["write email","finish homework","call mom","clean room"]
print("the list of what we are going to ", todo_list)

# Remove "call mom" from the list
print("Mom is coming. We don't need to call her.")
todo_list.remove("call mom")

# Print the updated list
print("the list of what we are going to ", todo_list)

# Remove "clean room" from the list and print the final list
todo_list.remove("clean room")
print("I spend 30 minutes cleaning the room! Here is the rest of thing i need to do: ",todo_list)