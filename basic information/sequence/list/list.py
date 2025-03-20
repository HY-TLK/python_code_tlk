# Creating a List
my_list = [1, 2, 3, 4, 5]

# Accessing Elements
print(my_list[0])  # Output: 1

# Slicing
print(my_list[1:4])  # Output: [2, 3, 4]

# Adding Elements
my_list.append(6)            # Add to end of list
my_list.extend([7, 8, 9])    # Add multiple elements
my_list.insert(2, 10)        # Insert at specific position

# Removing Elements
my_list.remove(3)  # Remove first matching element
popped = my_list.pop()       # Remove and return last item
my_list.clear()    # Empty the list

# Modifying Elements
my_list[0] = 100  # Modify element at specific index

# Finding Elements
print(my_list.count(2))  # Number of occurrences
print(my_list.index(4))  # Index of first occurrence

# Sorting and Reversing
num_list = [5, 2, 8, 1, 3]
num_list.sort()   # Sort in ascending order
num_list.reverse()# Reverse the list

# Copying Lists
copy_list = num_list.copy()  # Shallow copy
deep_copy_list = num_list[:] # Slice copy

# Nested Lists
nested_list = [[1, 2], [3, 4], [5, 6]]
# Shallow vs Deep Copy
import copy
shallow_copy = copy.copy(nested_list)
deep_copy = copy.deepcopy(nested_list)

# List Comprehension
squares = [x**2 for x in range(10)]  # Squares of 0-9
even_squares = [x**2 for x in range(10) if x % 2 == 0]  # Squares of even numbers

# Other List Operations
# Merging Lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
merged_list = list1 + list2  # [1, 2, 3, 4, 5, 6]

# Repeating Lists
repeated_list = list1 * 3  # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# Iterating Through a List
for item in my_list:
    print(item)

# Enumerating a List
for index, value in enumerate(my_list):
    print(f"Index: {index}, Value: {value}")