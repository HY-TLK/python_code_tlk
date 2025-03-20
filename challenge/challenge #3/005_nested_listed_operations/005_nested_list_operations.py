#-----------------------------------------------------------------------------
# Name:        005_nested_list_operations
# Purpose:     Work with a nested list to access, modify, and manipulate data.
#
# Author:      Harry Yang
# Created:     18-Mar-2025
#-----------------------------------------------------------------------------

# Create a list students which contains the following data about three students:
students = [['Alice', 25, 'Physics'],
            ['Bob', 22, 'Chemistry'],
            ['Charlie', 24, 'Biology']]

# Change Bob's age to 23 and his major to 'Mathematics'.
students[1][1] = 23
students[1][2] = "Mathematics"

# Print the updated students list.
print("Change Bob's age to 23 and his major to 'Mathematics'")
print(students)

# Access and print the name of the student who is studying 'Biology'.
print("we need a student who is studying 'Biology'")
for i in range(len(students)):
    if students[i][2] == "Biology":
        print(students[i][0])