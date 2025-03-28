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


# 16. **Recursive Dictionary Sum**
print("\nQuestion 16: ")
#     - **Problem**: Traverse a nested dictionary (e.g., `{'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}`)
sample_dict_16 = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
#     and sum all values. The output should be `6`.


# 18. **Power Set Generation**
print("\nQuestion 18: ")
#     - **Problem**: Generate all subsets of a set. For example, the power set of `{1,2}` is `{ }, {1}, {2}, {1,2}`.
sample_set_18 = {2,5,7}
list_18 = list(sample_set_18)
res = [[]]
for each in list_18:
    res += [subset + [each] for subset in res]
print(res)

# 25. **String Parsing into Dictionary**
print("\nQuestion 25: ")
#     - **Problem**: Convert a string like `"apple:1, banana:2, orange:3"` into a dictionary `{'apple':1, 'banana':2, 'orange':3}`.
sample_string_25 = "apple:1, banana:2, orange:3"
dict_25 = {k.strip():int(v) for k,v in (pairs.split(":") for pairs in sample_string_25.split(","))}
print(dict_25)

# 27. **Matrix Transposition**
print("\nQuestion 27: ")
#     - **Problem**: Transpose a matrix (e.g., `[[1,2,3], [4,5,6]]`) and store the result in a dictionary where keys are original row indices and values are column lists: `{0: [1,4], 1:[2,5], 2:[3,6]}`.
matrix = [[1,2,3],
          [4,5,6]]
dict_27 = {i:list(col) for i,col in enumerate(zip(*matrix))}
print(dict_27)

# 34. **Nested Dictionary Dynamic Access**
print("\nQuestion 34: ")
#     - **Problem**: Given a nested dictionary like `{'x': {'y': {'z': 10}}}`,
#     write a function to access the value using a key path (e.g., `['x','y','z']` returns `10`).
sample_dict_34 = {'x': {'y': {'z': 10}}}
user_input_34 = input("please enter your key path: ")
keys = user_input_34.split(",")