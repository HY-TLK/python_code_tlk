# ### **Exercise 1: Basic Dictionary Operations**
print("Exercise 1 : ")
# Write code to:
# 1. Create a dictionary `student` using the `dict()` function with keyword arguments, containing the following key-value pairs:
#    - Key `"name"`, value `"Alice"`
#    - Key `"age"`, value `20`
#    - Key `"major"`, value `"Computer Science"`
student = {"name":"Alice","age":20,"major":"Computer Science"}
print(student)
# 2. Add a new key-value pair: `"grade": "A"`
student["grade"] = "A"
print(student)
# 3. Update the value of `"age"` to `21`
student.update({"age":21})
print(student)
# 4. Remove the key `"major"`
del student["major"]
print(student)
# 5. Print the final dictionary.
print("final dictionary: ",student)
print()

# ### **Exercise 2: Key Uniqueness Validation**
print("Exercise 2 : ")
# Write code to:
# 1. Create an empty dictionary `word_counts`.
# 2. Count the occurrences of each word in the following list and store the results in the dictionary:
#    words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
counts = list(map(lambda word: words.count(word), words))
# 3. Print the dictionary, ensuring keys are unique and values are cumulative counts.
word_counts = dict(zip(words, counts))
print(word_counts)
print()

# ### **Exercise 3: Using `fromkeys()` Method**
print("Exercise 3 : ")
# Write code to:
# 1. Use `dict.fromkeys()` to create a dictionary `default_settings` with the following conditions:
#    - Keys are from the list `["volume", "brightness", "resolution"]`
#    - Default value for all keys is `100`
default_settings = dict.fromkeys(["volume","brightness","resolution"],100)
print(default_settings)
# 2. Update the value of `"resolution"` to `1920x1080`
default_settings["resolution"] = "1920x1080"
# 3. Print the updated dictionary.
print(default_settings)
print()

# ### **Exercise 4: Dynamic Dictionary Update**
print("Exercise 4 : ")
# Write code to:
# 1. Create an empty dictionary `inventory`.
inventory = {}
# 2. Dynamically add items and their quantities to the dictionary based on user input until the user types `"done"`.
#    - Example input format: `"apple 5"` means adding `"apple": 5`
# 3. After the user finishes, print the complete inventory dictionary.
while True:
    user_input = input("please enter your item: ")
    user_input = user_input.lower()
    if user_input != "done":
        splited = list(user_input.split())
        item = splited[0]
        quantity = splited[1]
        inventory[item] = int(quantity)
        print(inventory)
    else:
        print("thank you")
        break
print()

# ### **Exercise 5: Dictionary Merging**
print("Exercise 5 : ")
# Write code to:
# 1. Given two dictionaries:
#    dict1 = {"a": 1, "b": 2}
#    dict2 = {"b": 3, "c": 4}
# 2. Merge these two dictionaries, ensuring that:
#    - If keys are duplicated, keep the value from `dict2`.
# 3. Print the merged dictionary.
dict1 = {"a":1,"b":2}
dict2 = {"b":3,"c":4}
for letter in dict2:
    dict1[letter] = dict2[letter]
print(dict1)
print()

# ### **Exercise 6: Dictionary and Loops**
print("Exercise 6 : ")
# Write code to:
# 1. Extract all even numbers from the following list and store them in a dictionary `even_numbers`:
#    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#    - Keys should be the string representation of the even numbers (e.g., `"2"`), and values should be the integers themselves.
# 2. Print the dictionary `even_numbers`.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers_filtered = list(filter(lambda num: num % 2 == 0, numbers))
even_number = {}
for i in numbers_filtered:
    even_number[f"{i}"] = i
print(even_number)
print()

# ### **Exercise 7: Dictionary Filtering**
print("Exercise 7 : ")
# Write code to:
# 1. Given the dictionary:
#    prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "mango": 3.0}
prices = {"apple": 1.2, "banana": 0.5, "cherry": 2.5, "mango": 3.0}
# 2. Create a new dictionary `affordable` containing only key-value pairs where the value is less than `2.0`.
affordable = {}
for key,value in prices.items():
    if value < 2:
        affordable[key] = value
print(affordable)

# 3. Print the new dictionary.
