# Compare Object Memory Addresses
print("Question1: ")
# - Create two lists: `c = [1, 2, 3]` and `d = [1, 2, 3]`.
c = [1, 2, 3]
d = [1, 2, 3]
# - Create two tuples: `e = (4, 5)` and `f = (4, 5)`.
e = (4,5)
f = (4,5)
# - Use `is` and `==` to compare their values and memory addresses.
print(c is d)
print(f is e)
print(c == d)
print(f == e)
print()

# Using `del` to Delete Slices
print("Question2: ")
# Given the list `x = [10, 20, 30, 40, 50, 60]`:
# - Remove elements from index 1 to 3 (excluding 3).
x = [10,20,30,40,50,60]
del x[1:3]
print(x)
# - Remove elements at all even indices (e.g., 0, 2, 4…).
x = [10,20,30,40,50,60]
del x[::2]
print(x)
# - Clear the entire list.
x = [10,20,30,40,50,60]
del x [:]
print(x)
print()

# Type Conversion & Tuple Concatenation
print("Question3: ")
# - Convert the string `"Python"` into a list.
print(list("Python"))
# - Convert each character into a single-element tuple (e.g., `('P',)`).
print(tuple((each,) for each in "Python"))
# - Merge all tuples into a new tuple.
print(tuple (each for each in "Python"))
print()

# Multi-Condition Sorting
print("Question4: ")
# Sort the list `words = ["apple", "Banana", "cherry", "Date"]`:
words = ["apple","Banana","Date","cherry"]
# - **Primary condition**: Sort by string length (ascending).
# - **Secondary condition**: If lengths are the same, sort alphabetically (case-insensitive).
words_sorted = sorted(words,key=lambda word:(len(word),word.lower()))
print(words_sorted)
print()

# Using `zip` to Merge Data
print("Question5: ")
# Given:
# names = ["Alice", "Bob", "Charlie"]
names = ["Alice","Bob","Charlie"]
# scores = [85, 90, 78]
scores = [85,90,78]
# - Merge them into a list of tuples, where each tuple is `(name, score)`.
print(tuple(zip(names,scores)))
print()

# Using `map` & `filter` Together
print("Question6: ")
# Given `nums = [1, 2, 3, 4, 5]`:
nums = [1,2,3,4,5]
# - Use `map` to square each number.
nums_square = list(map(lambda x: x**2,nums))
print(nums_square)
# - Use `filter` to keep only even squared numbers.
num_filter = list(filter(lambda x: x%2,nums_square))
print(num_filter)
print()


# Reverse Iterator & String Join
print("Question7: ")
# - Convert `"hello"` into a reverse iterator.
word_reversed = reversed("Python")
# - Join the reversed characters into a new string.
print(" ".join(word_reversed))
print()

# Enumerate for Structured Data
print("Question8: ")
# Given `fruits = ["apple", "banana", "cherry"]`:
fruits = ["apple","banana","cherry"]
# - Generate a new list of tuples `(index, name)`, starting index from 1.
print(list(enumerate(fruits,1)))
print()

# Text Processing
print("Question9: ")
# Given `text = "Python is fun"`:
text = "Python is fun"
# - Split it into words.
text_split = text.split()
# - Convert all words to uppercase.
text_split = [each.upper() for each in text_split]
print(text_split)
# - Sort words by length (descending).
text_split_sorted = sorted(text_split,key = len)
print(text_split_sorted)
# - Join the result with commas.
text_final = ",".join(text_split_sorted)
print(text_final)
print()

# Multi-Level Sorting
print("Question10: ")
# Given:
# students = [("Alice", 22), ("Bob", 19), ("Charlie", 23)]
students = [("Alice",22),("Bob",19),("Charlie",23),("Ali",19)]
# - Primary condition: Sort by age (ascending).
# - Secondary condition: If ages are the same, sort names in descending order.
students_sorted = sorted(students,key=lambda student: (student[1],-ord(student[0][0])))
print(students_sorted)
print()

# Merging Unequal-Length Lists
print("Question11: ")
# Given:
# keys = ["name", "age", "city"]
# values1 = ["Alice", 25]
# values2 = ["Bob", 30, "Paris", "Engineer"]
keys = ["name","age","city"]
values1 = ["Alice",25]
values2 = ["Bob",30,"Paris","Engineer"]
# - Use `itertools.zip_longest` to merge them, filling missing values with `"None"`.
import itertools
print(list(itertools.zip_longest(keys,values1,values2)))
print()

# Filter & Convert Mixed Data Types
print("Question12: ")
# Given `data = [1, "apple", 3, "banana", 5, 7.5, 9]`:
data = [1,"apple",3,"banana",5,7.5,9]
# - Filter out only integers.
data_filter1 = list(filter(lambda x:type(x) == int, data))
print(data_filter1)
# - Square the integers.
data_filter1_square = [i ** 2 for i in data_filter1]
# - Output the result as a list.
print(data_filter1_square)
print()

# Advanced Text Analysis
print("Question13: ")
# Given `text = "Hello World! Python is AWESOME."`:
import string
text = "Hello World! Python is AWESOME!"
# - Split words (remove punctuation).
words = text.split()
cleaned_words = [word.strip(string.punctuation) for word in words]
print(cleaned_words)
# - Filter words that contain at least one lowercase letter.
words_filtered = list(filter(lambda x: x.isupper() == False, cleaned_words))
print(words_filtered)
# - Sort by length (ascending), and by descending order if lengths are equal.
words_sorted = sorted(words_filtered, key = lambda word:len(word))
print(words_sorted)