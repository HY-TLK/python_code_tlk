# Basic information about dictionaries

# Example 1: Difference between set and dictionary
x = {"hallo", "world"}
print(type(x))  # This is a set, not a dict
# Note: Dictionaries require colons for key-value pairs
print()

# Example 2: Proper dictionary creation and access
y = {"Python": "nohtyP", "hallo": "ollah"}
print(type(y))  # Output: <class 'dict'>
# The part before the colon is called a key; The part after is a value
print(y["Python"])  # Access value by key
print()

# Six ways to create a dictionary
# Method 1: Direct initialization (shown above)

# Method 2: Using dict() with keyword arguments
dict_keyword = dict(harry="Harry", yang="Yang")
print(dict_keyword)
print()

# Method 3: Pass a list of key-value tuples to dict()
dict_tuples = dict([("name", "harry"), ("age", "16"), ("gender", "male")])
print(dict_tuples)
print()

# Method 4: Pass a dictionary to dict()
dict_nested = dict({"Python": "nohtyP", "hallo": "ollah"})
print(dict_nested)
print()

# Method 5: Mix dictionary and keyword arguments
dict_mixed = dict({"Python": "nohtyP"}, hallo="ollah")
print(dict_mixed)
print()

# Method 6: Using zip() function
dict_zip = dict(zip(["Python", "hallo"], ["nohtyP", "ollah"]))
print(dict_zip)
print()

# Create using fromkeys()
dict_fromkeys = dict.fromkeys("three", 3)  # String "three" is iterated character-wise
print(dict_fromkeys)  # Output: {'t': 3, 'h': 3, 'r': 3, 'e': 3}

# Delete operations
dict_fromkeys.pop("h")  # Remove key 'h'
print(dict_fromkeys)    # Output: {'t': 3, 'r': 3, 'e': 3}

dict_fromkeys.popitem()  # Remove last inserted item (Python 3.7+)
print(dict_fromkeys)     # Output: {'t': 3, 'r': 3}

del dict_fromkeys["r"]   # Direct deletion
print(dict_fromkeys)     # Output: {'t': 3}

# Modify/Add items
dict_fromkeys["t"] = 111  # Modify existing key
print(dict_fromkeys)      # Output: {'t': 111}

dict_fromkeys["y"] = 222  # Add new key-value pair
print(dict_fromkeys)      # Output: {'t': 111, 'y': 222}