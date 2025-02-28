# ================ Set Fundamentals ================
# Checking collection types
print(type({}))          # <class 'dict'> (Empty braces create dictionary)
print(type({"hello"}))   # <class 'set'> (Single element set)
print(type({"hello":1})) # <class 'dict'> (Key-value pairs make dictionary)
print()

# ================ Set Creation Methods ================
# 1. Literal syntax with unique elements
programming_set = {"Python", "Java", "C++", "Python"}  # Duplicates auto-removed
print("Literal Set:", programming_set)  # Output order may vary

# 2. Set comprehension for processing data
processed_chars = {char.lower() for char in "HelloWorld"}  # Case-insensitive processing
print("Comprehension Set:", processed_chars)  # {'h', 'e', 'l', 'o', 'w', 'r', 'd'}

# 3. Constructor conversion from iterables
name_set = set("Mississippi")  # Auto-deduplication of characters
print("Constructor Set:", name_set)  # {'M', 'i', 's', 'p'}
print()

# ================ Core Set Operations ================
# Membership testing
print("'s' in name_set:", 's' in name_set)  # True

# Set iteration (order not guaranteed)
print("Set elements:")
for element in programming_set:
    print(f"- {element}")

# Unique values demonstration
numbers = [2, 3, 2, 5, 5, 1]
unique_numbers = set(numbers)  # Remove duplicates
print("\nUnique Numbers:", unique_numbers)  # {1, 2, 3, 5}
print()

# ================ Set Relationships ================
set_a = {1, 2, 3}
set_b = {3, 4, 5}

# Disjoint check (no common elements)
print("Disjoint check:", set_a.isdisjoint({4, 5, 6}))  # True

# Subset operations
print("Subset check:", {2, 3}.issubset(set_a))      # True
print("Proper subset:", {1, 2} < set_a)             # True
print("Equal or subset:", set_a <= set_a)           # True

# Superset operations
print("Superset check:", set_a.issuperset({1, 2}))  # True
print("Proper superset:", set_a > {1})              # True
print()

# ================ Mathematical Operations ================
# Union (combine elements)
print("Union:", set_a.union(set_b))      # {1, 2, 3, 4, 5}
print("Union operator:", set_a | set_b)  # Equivalent

# Intersection (common elements)
print("Intersection:", set_a & set_b)    # {3}

# Difference (elements in A not in B)
print("Difference:", set_a - set_b)     # {1, 2}

# Symmetric difference (unique to each set)
print("Symmetric Difference:", set_a ^ set_b)  # {1, 2, 4, 5}
print()

# ================ Set Modification Methods ================
# Adding elements
programming_set.add("JavaScript")
print("After adding:", programming_set)

# Safe removal (no error if missing)
programming_set.discard("Ruby")
print("After discard:", programming_set)

# Random element removal
removed = programming_set.pop()
print(f"Removed '{removed}':", programming_set)

# Clear all elements
programming_set.clear()
print("Cleared set:", programming_set)
print()

# ================ Advanced Operations ================
# Shallow copy demonstration
original = {1, 2, 3}
copied = original.copy()
copied.add(4)
print("Original:", original)  # {1, 2, 3}
print("Copy:", copied)        # {1, 2, 3, 4}

# Set comprehension with condition
even_squares = {x**2 for x in range(10) if x%2 == 0}
print("\nEven Squares:", even_squares)  # {0, 4, 16, 36, 64}

# Nested sets using frozenset
immutable_set = frozenset([1, 2, 3])
nested_set = {immutable_set, 4, 5}
print("\nNested Set:", nested_set)  # {frozenset({1, 2, 3}), 4, 5}

# ================ Update Methods ================
active_set = {"a", "b"}
active_set.update(["c", "d"])  # Add multiple elements
print("\nAfter update:", active_set)  # {'a', 'b', 'c', 'd'}

active_set.intersection_update({"a", "c", "e"})  # Keep common elements
print("After intersection update:", active_set)  # {'a', 'c'}

active_set.difference_update({"a"})  # Remove specific elements
print("After difference update:", active_set)  # {'c'}

active_set.symmetric_difference_update({"c", "d"})  # Toggle elements
print("After symmetric update:", active_set)  # {'d'}