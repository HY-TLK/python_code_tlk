# ================ Basic List ================
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

# ================ Exercises ================
'''
1. Basic Indexing
   Goal: Print Wednesday and Sunday
   Requirement: Use both positive and negative indexing
'''
print("\n=== Exercise 1 ===")
print(week_days[2], week_days[-1])  # Positive index 2 is Wednesday, negative index -1 is Sunday

'''
2. Slicing
   Goal: Get the list of workdays (Monday to Friday)
   Requirement: Use slicing syntax
'''
print("\n=== Exercise 2 ===")
work_days = week_days[:5]  # Slice from 0 to 4 (excluding 5)
print("Workdays:", work_days)  # ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']

'''
3. Modifying Elements
   Goal: Change the weekend days to Chinese
   Requirement: Modify the original list
'''
print("\n=== Exercise 3 ===")
week_days[-2:] = ['Saturday', 'Sunday']  # Modify the last two elements
print("Modified list:", week_days)  # ['Monday', ..., 'Friday', '周六', '周日']

'''
4. Adding Elements
   Goal: Insert "Special Day" after Friday
   Requirement: Use two methods (insert() and slicing)
'''
print("\n=== Exercise 4 ===")
# Method 1: insert()
week_days.insert(4, "Special Day")  # Insert at index 4
# Method 2: Slicing and concatenation
# week_days = week_days[:4] + ["Special Day"] + week_days[4:]
print("After insertion:", week_days)

'''
5. Removing Elements
   Goal: Remove "Special Day" and retrieve the removed element
   Requirement: Use pop() and remove() methods
'''
print("\n=== Exercise 5 ===")
# Method 1: pop(index)
popped = week_days.pop(4)  # Remove element at index 4
# Method 2: remove(value)
# week_days.remove("Special Day")
print(f"Removed element: {popped}, Remaining list: {week_days}")

'''
6. Sorting
   Goal: Sort the days by word length (keep the original list)
   Requirement: Use sorted() and sort() methods
'''
print("\n=== Exercise 6 ===")
# Method 1: Create a new list
sorted_by_length = sorted(week_days, key=len)
# Method 2: In-place sorting
# week_days.sort(key=lambda x: len(x))
print("Sorted by length:", sorted_by_length)

'''
7. List Comprehension
   Goal: Generate a list of abbreviations (first 3 letters)
   Requirement: Preserve the original list
'''
print("\n=== Exercise 7 ===")
abbreviations = [day[:3] for day in week_days]
print("Abbreviations:", abbreviations)  # ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

'''
8. Iteration
   Goal: Add numbering to each day
   Requirement: Output format "1. Monday"
'''
print("\n=== Exercise 8 ===")
for idx, day in enumerate(week_days, 1):  # Start numbering from 1
    print(f"{idx}. {day}")

'''
9. List Merging
   Goal: Create a nested list containing workdays and weekends
   Requirement: Use two methods
'''
print("\n=== Exercise 9 ===")
work_days = week_days[:5]
weekends = week_days[5:]
# Method 1: Direct concatenation
combined = [work_days, weekends]
# Method 2: Append lists
# combined = []
# combined.append(work_days)
# combined.append(weekends)
print("Nested list:", combined)

'''
10. Advanced Operations
    Goal: Find the day with the most letters
    Requirement: Use max() and a generator expression
'''
print("\n=== Exercise 10 ===")
longest_day = max(week_days, key=lambda x: len(x))
print("Longest day:", longest_day)  # Wednesday

'''
11. Counting
    Goal: Count the number of days containing the letter 'a'
    Requirement: Use list comprehension
'''
print("\n=== Exercise 11 ===")
a_days = [day for day in week_days if 'a' in day.lower()]
print("Days containing 'a':", len(a_days), "days")  # Saturday/Sunday

'''
12. Reversing
    Goal: Move weekends to the end of the list
    Requirement: Keep the order of other days unchanged
'''
print("\n=== Exercise 12 ===")
week_days = week_days[5:] + week_days[:5]  # Reorganize using slicing
print("Weekends at the end:", week_days)