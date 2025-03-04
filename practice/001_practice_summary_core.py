# 11. **List Rotation**
print("\nQuestion *11: ")
#     - **Problem**: Implement a function to rotate a list to the right by `k` positions.
#     For example, rotating `[1,2,3,4,5]` by 2 results in `[4,5,1,2,3]`.
sample_list_11 = [1,2,3,4,5]
user_input_11 = int(input("Enter a number: "))
n = len(sample_list_11)
user_input_11 %= n
list_11 = sample_list_11[-user_input_11:] + sample_list_11[:-user_input_11]
print(list_11)


# 12. **Dynamic Dictionary Query**
print("\nQuestion 12: ")
#     - **Problem**: Given a nested dictionary:
students_dict_12 = {'student1': {'name': 'A', 'age':20},
                    'student2': {'name': 'B', 'age':22},
                    'student3': {'name': 'C', 'age':19}}
#       Write a function to query a student’s age by name. If the name doesn’t exist, prompt the user to re-enter.
user_input_12 = input("Enter a name: ")
for s in students_dict_12.values():
    if user_input_12 == s['name']:
        print(s['age'])
        break
    else:
        print("You have not entered the name.")