#-----------------------------------------------------------------------------
# Name:        003_remove_items_from_a_list
# Purpose:     Remove an item from a list.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list todo_list
tool_list = ["write email","finish homework","call mom","clean room"]

# Remove "call mom" from the list
tool_list.remove("call mom")

# Print the updated list
print(tool_list)

# Remove "clean room" from the list and print the final list
tool_list.remove("clean room")
print(tool_list)