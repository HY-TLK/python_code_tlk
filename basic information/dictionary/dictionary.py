# === Basic Dictionary Operations ===

# Example 1: Set vs Dictionary
x = {"hallo", "world"}
print(type(x))  # This is a set, not a dictionary
# Note: Dictionaries require key-value pairs with colons (:)
print()

# Example 2: Dictionary Creation and Access
y = {"Python": "nohtyP", "hallo": "ollah"}
print(type(y))  # Output: <class 'dict'>
print(y["Python"])  # Access value using key
print()

# === Six Dictionary Creation Methods ===

# Method 1: Direct initialization (already shown)

# Method 2: Using dict() with keyword arguments
dict_keyword = dict(harry="Harry", yang="Yang")
print("Keyword creation:", dict_keyword)
print()

# Method 3: List of key-value tuples
dict_tuples = dict([("name", "harry"), ("age", 16), ("gender", "male")])
print("Tuple list creation:", dict_tuples)
print()

# Method 4: Nested dictionary
dict_nested = dict({"Python": "nohtyP", "hallo": "ollah"})
print("Nested dict creation:", dict_nested)
print()

# Method 5: Mixed style creation
dict_mixed = dict({"Python": "nohtyP"}, hallo="ollah")
print("Mixed creation:", dict_mixed)
print()

# Method 6: Using zip() function
keys = ["Python", "hallo"]
values = ["nohtyP", "ollah"]
dict_zip = dict(zip(keys, values))
print("Zip creation:", dict_zip)
print()

# === Dictionary Operations ===

# Create using fromkeys()
dict_fromkeys = dict.fromkeys("three", 3)  # Creates keys from string characters
print("Fromkeys:", dict_fromkeys)  # Output: {'t': 3, 'h': 3, 'r': 3, 'e': 3}

# Deletion operations
dict_fromkeys.pop("h")  # Remove specific key
print("After pop('h'):", dict_fromkeys)

dict_fromkeys.popitem()  # Remove last inserted item (Python 3.7+)
print("After popitem():", dict_fromkeys)

del dict_fromkeys["r"]  # Direct deletion
print("After del:", dict_fromkeys)

# Modification and addition
dict_fromkeys["t"] = 111  # Update existing key
print("After update:", dict_fromkeys)

dict_fromkeys.update({"t": 100})  # Update using update()
print("After update():", dict_fromkeys)

dict_fromkeys.update(t=777)  # Keyword-style update
print("After keyword update:", dict_fromkeys)

dict_fromkeys["y"] = 222  # Add new key-value pair
print("After addition:", dict_fromkeys)

# === Dictionary Methods ===

# get() method
dict_get = dict_fromkeys.get("s", "there is no 's' in it")
print("\nGet non-existent key:", dict_get)

# setdefault() method
value_s = dict_fromkeys.setdefault("s", "there is no 's' in it")
print("Setdefault result:", value_s)
print("After setdefault:", dict_fromkeys)

# Dictionary view objects
keys = dict_fromkeys.keys()
values = dict_fromkeys.values()
items = dict_fromkeys.items()
print("\nView objects:")
print("Keys:", keys, type(keys))
print("Values:", values, type(values))
print("Items:", items, type(items))

# Demonstrate dynamic nature
dict_fromkeys.pop("s")
print("\nAfter popping 's':", dict_fromkeys.items())

# === Dictionary Features ===

print("\nLength:", len(dict_fromkeys))
print("Membership check:", "y" in dict_fromkeys)

# Conversion to list
key_list = list(dict_fromkeys.keys())
print("\nKey list:", key_list)

# Iterator and reversal
key_iterator = iter(dict_fromkeys)
print("\nIterator:", key_iterator)
reversed_items = list(reversed(dict_fromkeys.items()))
print("Reversed items:", reversed_items)

# === Nested Dictionaries ===

# Dictionary of dictionaries
gradebook = {
    "harry": {"English": 10, "Math": 100},
    "yang": {"English": 20, "Math": 200}
}
print("\nNested access:", gradebook["harry"]["English"])

# Dictionary of lists
scores = {
    "harry": [10, 100],
    "yang": [20, 200]
}
print("List access:", scores["harry"][1])

# === Dictionary Comprehensions ===

# Example 1: Character to ASCII mapping
char_map = {x: ord(x) for x in "harry"}
print("\nCharacter ASCII mapping:", char_map)
"""
Explanation:
- Iterates over each character in "harry"
- Creates key-value pairs where:
  - Key: character (x)
  - Value: ASCII code (ord(x))
Result: {'h': 104, 'a': 97, 'r': 114, 'y': 121}
Note: Duplicate 'r' is overwritten - dictionaries keep unique keys
"""

# Example 2: Nested loop comprehension
number_pairs = {x: y for x in [1, 3, 5] for y in [2, 4, 6]}
print("Nested loop result:", number_pairs)
"""
Explanation:
- Outer loop: x in [1, 3, 5]
- Inner loop: y in [2, 4, 6]
- Creates key-value pairs for ALL combinations
- BUT: Later values overwrite earlier ones for same key
Final result: {1: 6, 3: 6, 5: 6}
Because:
- 1 gets values 2, 4, 6 (last is 6)
- 3 gets values 2, 4, 6 (last is 6)
- 5 gets values 2, 4, 6 (last is 6)
"""