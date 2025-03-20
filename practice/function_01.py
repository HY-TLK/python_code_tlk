# ## Exercise 1: Simple Function Definition
# Write a function called `greet` that prints "Hello, World!" when called.
def greet():
    print("hello world")


greet()


# ## Exercise 2: Function with a Parameter
# Write a function called `greet_user` that takes a parameter `name` and prints "Hello, {name}!".
def greet_user(name):
    print(f"hello! {name}")


greet_user("harry")


# ## Exercise 3: Function with Return Value
# Write a function called `add` that takes two parameters `a` and `b`, and returns their sum.
def add(a, b):
    return a + b


print(add(3, 5))


# ## Exercise 4: Default Parameter
# Write a function called `greet_user` that takes a parameter `name` and an optional parameter `greeting` with a default value of "Hello". The function should print "{greeting}, {name}!".
def greet_user(name, greeting="hello"):
    print(f"{greeting}!{name}")


greet_user("harry")
greet_user("harry", greeting="hi")


# ## Exercise 5: Variable-Length Arguments
# Write a function called `sum_numbers` that takes any number of arguments and returns their sum.
def sum_numbers(*args):
    return sum(args)


print(sum_numbers(1, 2, 3, 9))


# ## Exercise 6: Keyword Arguments
# Write a function called `describe_pet` that takes two parameters `animal_type` and `pet_name`, and prints a description of the pet.
def describe_pet(animal_type, pet_name): \
        print(f"the name of the {animal_type} is {pet_name}")


describe_pet(animal_type="dog", pet_name="wangcai")


# ## Exercise 7: Return a Dictionary
# Write a function called `make_person` that takes `first_name`, `last_name`, and an optional parameter `age`, and returns a dictionary containing the person's information.
def make_person(first_name, last_name, age=None, **kwargs):
    person = {"first name": first_name,
              "last name": last_name}
    if age is not None:
        person["age"] = age
    person.update(kwargs)
    print(person)


make_person("harry", "yang", age=16, gender="male")


# ## Exercise 8: Conditional Statements in Functions
# Write a function called `check_number` that takes a number `num` and returns "Positive" if it's greater than 0, "Zero" if it's 0, and "Negative" if it's less than 0.
def check_number(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("negative")
    else:
        print("the number is 0")


check_number(1)
check_number(-1)
check_number(0)


# ## Exercise 9: Loops in Functions
# Write a function called `print_numbers` that takes a number `n` and prints all numbers from 1 to n.
def print_numbers(n):
    for num in range(1, n + 1):
        print(num, end=" ")


print_numbers(5)
print()


# ## Exercise 10: Comprehensive Function
# Write a function called `calculate_statistics` that takes a list of numbers and returns a dictionary with the maximum, minimum, average, and sum of the numbers.
def calculate_statistics(*args):
    statistics = {"maxium": max(args),
                  "minium": min(args),
                  "averages": sum(args) / len(args),
                  "sum": sum(args)}
    print(statistics)


calculate_statistics(1, 2, 3, 6, 7, 8, 9)


# ## Exercise 11: Collecting Positional Arguments
# Write a function called `print_args` that takes any number of positional arguments and prints each one.
def print_args(*args):
    for arg in args:
        print(arg, end=" ")


print_args(1, 2, 3, "aa")
print()


# ## Exercise 12: Collecting Keyword Arguments
# Write a function called `print_kwargs` that takes any number of keyword arguments and prints each key-value pair.
def print_kwargs(**kwargs):
    print(kwargs)


print_kwargs(name="harry", age=16)


# ## Exercise 13: Mixing Argument Types
# Write a function called `process_data` that takes a regular parameter `a`, any number of positional arguments `*b`, and any number of keyword arguments `**c`.
# The function should print the value of `a`, the length of `b`, and all key-value pairs in `c`.
def process_data(a, *b, **c):
    print(a, len(b), c)


process_data("hahaha", 2, 3, 4, 5, name="harry", gender="male")


# ## Exercise 14: Unpacking and Collecting Arguments
# Write a function called `sum_all` that takes any number of arguments,
# which can be individual numbers or lists/tuples of numbers. The function should return the sum of all numbers.
def sum_all(*args):
    total = 0
    for arg in args:
        if isinstance(arg, (list, tuple)):
            total += sum_all(*arg)
        elif isinstance(arg, (int, float)):
            total += arg
        else:
            continue
    return total


print(sum_all([1, 2, [3, (2, 11)]]))


# ## Exercise 15: Complex Parameter Handling
# Write a function called `handle_parameters` that takes a regular parameter `a`,
# an optional parameter `b` with a default value of 2,
# any number of positional arguments `*args`, and two keyword parameters `c` (with a default value of 3)
# and `d` (without a default value).
# The function should print all parameter values and return a tuple containing all the values.
def handle_parameters(a, b=2, *args, d, c=3):
    return a, b, *args, c, d


print(handle_parameters(1, 3, 123, 234, c=9, d=100))

'''
the order of arguments:
1. **Positional Arguments**  
2. **Positional Default Arguments**  
3. **Variable Positional Arguments (`*args`)** (Collects additional positional arguments)  
4. **Keyword-Only Arguments**  
5. **Keyword-Only Default Arguments**  
6. **Variable Keyword Arguments (`**kwargs`)** (Collects additional keyword arguments)
'''
