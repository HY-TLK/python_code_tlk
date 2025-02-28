# ================ Basics of Hashing ================
# Hashing is a process of converting an object into a unique integer value.

# 1. Hash value of integers
print(hash(1))      # Output: 1 (small integers return themselves)
print(hash(100))    # Output: 100
print(hash(10**18)) # Output: 1000000000000000000 (large integers may vary by Python version)

# 2. Hash value of floats
print(hash(1.0))       # Output: 1 (same as hash(1))
print(hash(3.14159))   # Output: 326490430436040707 (complex calculation)
print(1.0 == 1)        # Output: True (equality affects hash)

# 3. Immutable objects are hashable
# Tuple with immutable elements
valid_tuple = (1, "hello", 3.14)
print(hash(valid_tuple))  # Output: -7273373080520386784

# Error: Tuple with mutable elements
# invalid_tuple = (1, [2], 3)  # TypeError: unhashable type: 'list'

# ================ Hashable Keys in Dictionaries and Sets ================
# Dictionary keys and set elements must be immutable (hashable).

# Valid keys/elements
valid_dict = {1: "one", "two": 2, (3,4): "tuple"}  # Immutable keys
valid_set = {1, "apple", (5,6)}                    # Immutable elements

# Invalid keys/elements
# invalid_dict = {[1]: "list"}  # TypeError: unhashable type: 'list'
# invalid_set = {{1: "one"}}    # TypeError: unhashable type: 'dict'

# ================ Mutable vs Immutable Objects ================
# Immutable objects are hashable; mutable objects are not.

# Immutable (hashable)
s = "hello"      # Hashable
t = (1, 2)       # Hashable
n = 100          # Hashable

# Mutable (unhashable)
lst = [1, 2]     # Unhashable
d = {"a": 1}     # Unhashable
set_obj = {1, 2} # Unhashable

print(hash(s))    # Output: -762667763575002594
# print(hash(lst)) # TypeError: unhashable type: 'list'

# ================ Practical Applications ================
# Example 1: Deduplication using sets
data = [1, 1.0, 2, 2.0, "2"]
unique_data = set(data)  # Automatically removes duplicates
print("Deduplicated data:", unique_data)  # Output: {1, 2, '2'}

# Example 2: Using tuples as dictionary keys
file1 = ("file1.txt", 1024, "2023-10-01")  # Tuple as key
file2 = ("file2.txt", 2048, "2023-10-01")
file_store = {file1: "Backup successful", file2: "Not backed up"}
print("File status:", file_store)

# ================ Key Takeaways ================
'''
1. Hashable objects must:
   - Be immutable (e.g., int, str, tuple).
   - Contain only hashable elements (e.g., no lists inside tuples).

2. Common hashable types:
   - Integers, floats, strings, tuples, frozensets.

3. Common unhashable types:
   - Lists, dictionaries, sets.

4. Practical uses of hashing:
   - Fast lookups in dictionaries.
   - Deduplication in sets.
   - File integrity checks.
'''