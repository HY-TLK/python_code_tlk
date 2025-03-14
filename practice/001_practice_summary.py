# 1. **Tuple and List Combination**
print("Question 1: ")
#    - **Problem**: Given a tuple containing elements of different types, e.g., `(1, "hello", [2,3,4], 5.6)`,
sample_tuple_1 = (1,"hello",[2,3,4],5.6)
#    write a program to store each element and its index in a dictionary.
#    For example, the output should be `{0:1, 1:"hello", 2:[2,3,4], 3:5.6}`.
index_1 = [i for i in range(len(sample_tuple_1))]
dict_1 = dict(zip(index_1, sample_tuple_1))
print(dict_1)

# 2. **Nested Dictionary Summation**
print("\nQuestion 2: ")
#    - **Problem**: Create a nested dictionary:
#      {
#          'fruits': {'apple': 3, 'banana': 5},
#          'vegetables': {'carrot': 2, 'tomato': 7}
#      }
sample_dict_2 = {"fruits":{"apple":3,"banana":5},"vegetables":{"carrot":2,"tomato":7}}
#      Then merge the values of each category into a new dictionary where keys are categories and values are the total quantities.
#      For example, the output should be `{'fruits': 8, 'vegetables':9}`.
sum_list = []
for key1, value1 in sample_dict_2.items():
    value_1 = list(value1.values())
    sum_list.append(sum(value_1))
dict_2 = dict(zip(sample_dict_2.keys(), sum_list))
print(dict_2)

# 3. **Set Operations**
print("\nQuestion 3: ")
#    - **Problem**: Given three sets `A = {1,2,3,4}`, `B={3,4,5,6}`, `C={4,5,6,7}`, compute `(A ∪ B) ∩ C` and output the resulting set.
A = {1,2,3,4}
B = {3,4,5,6}
C = {4,5,6,7}
print((A | B) & C )

# 4. **List Comprehension with Conditions**
print("\nQuestion 4: ")
#    - **Problem**: Generate a list of numbers from 1 to 100 that are divisible by 7,
#    then remove even numbers using list comprehension.
list_4_1 = [i for i in range(1,101) if i % 7 == 0]
list_4_2 = [x for x in list_4_1 if x % 2 == 0]
print(list_4_2)

# 5. **Dynamic String Formatting**
print("\nQuestion 5: ")
#    - **Problem**: Based on user input for name and age, generate a formatted welcome message.
name = "Alice"
age = 25
#    For example, input `"Alice"` and `25` should output `"Hello, Alice! You are 25 years old."`.
print(f"Hello, {name}, you are {age} years old.")

# 6. **Dictionary Key-Value Swap**
print("\nQuestion 6: ")
#    - **Problem**: Given a dictionary `{'a':1, 'b':2, 'c':3}`,
#    write a program to swap keys and values, resulting in `{1:'a', 2:'b',3:'c'}`.
sample_dict_6 = {"a":1,"b":2,"c":3}
dict_6 = {value:key for key, value in sample_dict_6.items()}
print(dict_6)

# 7. **Set Deduplication and Sorting**
print("\nQuestion 7: ")
#    - **Problem**:
#    Convert a list with duplicate elements `[3,1,2,3,4,2,5,1]` into a sorted list without duplicates,
#    e.g., `[1,2,3,4,5]`.
sample_list_7 = [3,1,2,3,4,2,5,1]
list_7 = sorted((set(sample_list_7)))
print(list_7)

# 8. **Nested Loop and List Generation**
print("\nQuestion 8: ")
#    - **Problem**: Create a 2D list where each inner list contains squares and fourth powers of the outer loop index.
#    For example, for indices 1-3, the output should be `[[1,4], [4,16], [9,36]]`.
list_8 = [[i**2,(i**2)*4] for i in range(1,4)]
print(list_8)

# 9. **Conditional Grading**
print("\nQuestion 9: ")
#    - **Problem**: Given a dictionary of student scores, e.g., `{'Alice':82, 'Bob':75, 'Charlie':90}`,
students = {"Alice":82,"Bob":75,"Charlie":90}
#    assign grades based on ranges:
#      - 90+ → A
#      - 80-89 → B
#      - Below 80 → C
for key, value in students.items():
    if value >= 90:
        print(key,"A")
    if 80 < value < 89:
        print(key,"B")
    else:
        print(key,"C")

# 10. **Infinite Loop with Exit Condition**
print("\nQuestion 10: ")
#     - **Problem**:
#     Prompt the user to input numbers continuously until two identical numbers are entered consecutively.
#     For example, inputs `5,3,7,7` should exit after the second `7`.
number_output = []
while True:
    user_input_10 = int(input("Enter a number: "))
    if user_input_10 not in number_output:
        number_output.append(user_input_10)
        print(number_output)
    else:
        print("You have already entered the number.")
        break

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


# 13. **Cartesian Product of Sets**
print("\nQuestion 13: ")
#     - **Problem**: Given two sets `
A = {1,2}
B = {'a','b'}
#     generate their Cartesian product: `[(1, 'a'), (1, 'b'), (2, 'a'), (2, 'b')]`.
list_13 = [(x,y) for x in A for y in B]
print(list_13)

# 14. **Nested List Depth Calculation**
print("\nQuestion 14: ")
#     - **Problem**: Given a nested list like `[1, [2, [3, 4], 5], 6]`,
#     write a function to calculate its depth (e.g., depth 3).

# 15. **Closest Element to Target**
print("\nQuestion 15: ")
#     - **Problem**: Find the element in a list closest to a target value.
#     For example, in `[4,7,5,9,2]` with target `6`, the closest element is `7` and `5`.
sample_list_15 = [4,7,5,9,2]
target_number = 6
print(f"Target number: {target_number} ")
delta = [abs(i - target_number) for i in sample_list_15]
closest_elements = [i for i in sample_list_15 if abs(i - target_number) == min(delta)]
print(closest_elements)

# 16. **Recursive Dictionary Sum**
print("\nQuestion 16: ")
#     - **Problem**: Traverse a nested dictionary (e.g., `{'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}`)
sample_dict_16 = {'a': 1, 'b': {'c': 2, 'd': {'e': 3}}}
#     and sum all values. The output should be `6`.


# 17. **Dynamic Dictionary Creation**
print("\nQuestion 17: ")
#     - **Problem**: Convert a string of key-value pairs (e.g., `"apple:1, banana:2, orange:3"`)
a = "apple:1,banana:2,orange:3"
#     into a dictionary `{'apple':1, 'banana':2, 'orange':3}`.
b = a.split(",")
c = [b[i].split(":") for i in range(0,len(b))]
zip_1 = [c[x][0] for x in range(0,len(c))]
zip_2 = [int(c[x][1]) for x in range(0,len(c))]
print(dict(zip(zip_1,zip_2)))


# 18. **Power Set Generation**
print("\nQuestion 18: ")
#     - **Problem**: Generate all subsets of a set. For example, the power set of `{1,2}` is `{ }, {1}, {2}, {1,2}`.
sample_set_18 = {2,5,7}
list_18 = list(sample_set_18)
res = [[]]
for each in list_18:
    res += [subset + [each] for subset in res]
print(res)

# 19. **Vowel Counting**
print("\nQuestion 19: ")
#     - **Problem**: Count the occurrences of vowels (`a, e, i, o, u`) in a string and store the results in a dictionary.
vowels = ['a', 'e', 'i', 'o', 'u']
#     For example, `"hello"` should result in `{'a':0, 'e':1, 'i':0, 'o':1, 'u':0}`.
user_input_19 = "hello"
times_list = []
for vowel in vowels:
    if vowel in user_input_19:
        times = user_input_19.count(vowel)
        times_list.append(times)
    if vowel not in user_input_19:
        times_list.append(0)
dict_19 = dict(zip(vowels,times_list))
print(dict_19)

# 20. **Infinite Loop with Exit Command**
print("\nQuestion 20: ")
#     - **Problem**: Continuously prompt the user for input until `exit` is entered.
#     Store all inputs in a list and output them at the end.
output_20 = []
while True:
    user_input_20 = input("type anything you want: ")
    if bool(user_input_20) == True:
        output_20.append(user_input_20)
        print(output_20)
    else:
        print("done!")
        break

# 21. **List Chunking**
print("\nQuestion 21: ")
#     - **Problem**: Implement a function `split_list(lst, chunk_size)` to split a list into sublists of size `chunk_size`.
#     For example, `[1,2,3,4,5,6]` with `chunk_size=2` becomes `[[1,2], [3,4], [5,6]]`.
sample_list_21 = [1,2,3,4,5,6]
user_input_21 = int(input("enter a chunk size: "))
nested_list_21 = [sample_list_21[i:i+user_input_21] for i in range(0,len(sample_list_21)) if i % user_input_21 == 0]
print(nested_list_21)

# 22. **Dictionary Key Order Reversal**
print("\nQuestion 22: ")
#     - **Problem**:reverse the order of keys in a dictionary
#     (e.g., `{'a':1, 'b':2, 'c':3}` becomes `{'c':3, 'b':2, 'a':1}`).
sample_dict_22 = {"a":1,"b":2,"c":3}
reverse_key_dict_22 = dict(zip(reversed(sample_dict_22.keys()),sample_dict_22.values()))
print(reverse_key_dict_22)

# 23. **Set Symmetric Difference**
print("\nQuestion 23: ")
#     - **Problem**: Compute the symmetric difference of two sets (elements in either set but not both).
#     For example, `{1,2,3}` and `{2,3,4}` results in `{1,4}`.
sample_set_23_1 = {1,2,3}
sample_set_23_2 = {2,3,4}
print(sample_set_23_1^sample_set_23_2)

# 24. **Prime Number Generation**
print("\nQuestion 24: ")
#     - **Problem**: Generate a list of prime numbers from 1 to 100 using list comprehension.
prime_number = [i for i in range (2,101) if all(i % x != 0 for x in range (2,i))]
print(prime_number)

# 25. **String Parsing into Dictionary**
print("\nQuestion 25: ")
#     - **Problem**: Convert a string like `"apple:1, banana:2, orange:3"` into a dictionary `{'apple':1, 'banana':2, 'orange':3}`.
sample_string_25 = "apple:1, banana:2, orange:3"
dict_25 = {k.strip():int(v) for k,v in (pairs.split(":") for pairs in sample_string_25.split(","))}
print(dict_25)

# 26. **Word Length Statistics**
print("\nQuestion 26: ")
#     - **Problem**: Read a text file, count the length of each word, store the results in a dictionary, and calculate the average word length.
text_file = "apple,banana,cherry,date,egg,flower,green"
len_text = [len(each) for each in text_file.split(",")]
dict_26 = {k.strip():int(v) for k,v in zip(text_file.split(","),len_text)}
print(dict_26)
average_len = sum(len_text) / len(len_text)
print(average_len)

# 27. **Matrix Transposition**
#     - **Problem**: Transpose a matrix (e.g., `[[1,2,3], [4,5,6]]`) and store the result in a dictionary where keys are original row indices and values are column lists: `{0: [1,4], 1:[2,5], 2:[3,6]}`.

# 28. **Dictionary Sorting and Filtering**
#     - **Problem**: Given `{'apple':5, 'banana':3, 'orange':4, 'grape':2}`, sort by values in descending order and filter values ≥3. The result should be `{'apple':5, 'orange':4, 'banana':3}`.

# 29. **Fibonacci Sequence Generation**
#     - **Problem**: Generate the first `n` Fibonacci numbers. For example, `n=5` results in `[0,1,1,2,3]`.

# 30. **Substring Matching**
#     - **Problem**: Check if a string contains a specific substring. For example, determine if `"hello world"` contains `"llo"`.

# 31. **Dictionary Key-Value Swap and Sorting**
#     - **Problem**: Swap keys and values in a dictionary and sort the new dictionary by keys. For example, `{'a':1, 'b':2}` becomes `{'1':'a', '2':'b'}`.

# 32. **Dynamic Set Updates**
#     - **Problem**: Maintain a set where users can continuously add elements until `stop` is entered. Output the set’s state after each addition.

# 33. **List Reversal with Slicing**
#     - **Problem**: Reverse a sublist in a list. For example, reversing indices 1-3 in `[1,2,3,4,5]` results in `[1,4,3,2,5]`.

# 34. **Nested Dictionary Dynamic Access**
#     - **Problem**: Given a nested dictionary like `{'x': {'y': {'z': 10}}}`,
#     write a function to access the value using a key path (e.g., `['x','y','z']` returns `10`).

# 35. **Set Union and Equality**
#     - **Problem**: Given two sets `A` and `B`, determine the condition under which `A ∪ B == A`. Verify this condition with code.

# 36. **Score Categorization**
#     - **Problem**: Classify a random number between 0 and 100:
#       - <30 → Warning
#       - 30-70 → Normal
#       - >70 → High
#     Use conditional branches to implement this.

# 37. **List Merging Without Sorting**
#     - **Problem**: Merge two lists `[1,3,5]` and `[2,4,6]` into `[1,2,3,4,5,6]` without using `sorted()`.

# 38. **Dictionary Default Values**
#     - **Problem**: Create a dictionary `scores` with default value `0`. When accessing a non-existent key, return `0`.
#     For example, `scores = {"a": 100}`, accessing `scores['b']` returns `0`.

# 39. **Exam Scoring System with Validation**
#     - **Problem**: Simulate an exam scoring system. Users input student names and scores (0-100).
#     If a score is below 60, prompt for re-entry. Store results in a dictionary until `exit` is entered.