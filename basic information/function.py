# 1. BASIC FUNCTION DEFINITION AND EXECUTION
def greet():
    """
    A simple function that prints a greeting message.
    This function doesn't take any arguments and doesn't return any value.
    """
    print("Hello, world!")

greet()  # Calling the function executes the print statement inside it

# 2. FUNCTION WITH POSITIONAL ARGUMENTS
def introduce(name):
    """
    Prints a personalized greeting.
    The 'name' parameter is a positional argument that must be provided when calling the function.
    """
    print(f"Hello, my name is {name}.")

introduce("Alice")  # The argument "Alice" is passed positionally to the function

# 3. FUNCTION WITH MULTIPLE ARGUMENTS
def calculate_area(length, width):
    """
    Calculates and returns the area of a rectangle.
    Both 'length' and 'width' are positional arguments that must be provided.
    """
    return length * width

area = calculate_area(5, 3)
print(f"The area of the rectangle is: {area}")

# 4. FUNCTION WITH CONDITIONAL RETURN
def divide(x, y):
    """
    Divides two numbers and handles division by zero.
    If the divisor (y) is zero, returns an error message instead of causing a runtime error.
    """
    if y == 0:
        return "Error: Division by zero is not allowed."
    else:
        return x / y

result = divide(10, 0)
print(result)  # Outputs the error message instead of a numerical result

# 5. FUNCTION WITH STRING MANIPULATION
def format_name(first, last):
    """
    Formats a full name with proper capitalization.
    Takes two string arguments and returns a formatted string.
    """
    return f"{first.capitalize()} {last.capitalize()}"

full_name = format_name("john", "doe")
print(f"Formatted name: {full_name}")

# 6. FUNCTION WITH DEFAULT ARGUMENTS
def greet_user(name, greeting="Hello"):
    """
    Greets the user with a customizable greeting.
    The 'greeting' parameter has a default value, making it optional when calling the function.
    """
    print(f"{greeting}, {name}!")

greet_user("Bob")          # Uses the default greeting "Hello"
greet_user("Bob", "Hi")    # Overrides the default greeting with "Hi"

# 7. FUNCTION WITH POSITIONAL-ONLY ARGUMENTS
def power(base, /, exponent):
    """
    Calculates the power of a number.
    The 'base' argument must be provided positionally due to the '/' syntax.
    """
    return base ** exponent

print(power(2, 3))     # Valid: both arguments are positional
print(power(2, exponent=3))  # Valid: 'base' is positional, 'exponent' is keyword
# print(power(base=2, exponent=3))  # Invalid: 'base' cannot be a keyword argument

# 8. FUNCTION WITH KEYWORD-ONLY ARGUMENTS
def create_user(*, username, email):
    """
    Creates a user with required keyword arguments.
    The '*' syntax enforces that 'username' and 'email' must be provided as keyword arguments.
    """
    print(f"Creating user: {username}, Email: {email}")

create_user(username="alice123", email="alice@example.com")
# create_user("alice123", "alice@example.com")  # Invalid: arguments must be keyword-only

# ==============================================================================
# 9. COLLECTING PARAMETERS
# ==============================================================================

# Using *args to collect positional arguments into a tuple
def myfunc(*args):
    """
    Demonstrates collecting positional arguments.
    *args packs all positional arguments into a tuple.
    """
    print(f"{len(args)} arguments")  # Number of arguments
    if len(args) >= 2:
        print(f"the second number is {args[1]}")  # Accessing specific argument
    print(args)  # Entire tuple of arguments

myfunc(1, 4, 8)  # Calling with multiple positional arguments


# Returning multiple values (implicitly returns a tuple)
def myfunc():
    """
    Returns multiple values which are packed into a tuple.
    """
    return 1, 2, 3

print(myfunc())  # Output: (1, 2, 3)
x, y, z = myfunc()  # Unpacking the tuple into variables


# Combining collected arguments with keyword-only arguments
def myfunc(*args, a, b):
    """
    Shows combining collected positional arguments with keyword-only arguments.
    *args collects positional arguments, while 'a' and 'b' must be keyword arguments.
    """
    print(f"Positional args: {args}, Keyword args: a={a}, b={b}")

myfunc(1, 2, a=3, b=4)  # Positional then keyword arguments

# 9. COLLECTING PARAMETERS
# Using *args to collect positional arguments into a tuple
def myfunc(*args):
    """
    Demonstrates collecting positional arguments.
    *args packs all positional arguments into a tuple.
    """
    print(f"{len(args)} arguments")  # Number of arguments
    if len(args) >= 2:
        print(f"the second number is {args[1]}")  # Accessing specific argument
    print(args)  # Entire tuple of arguments

myfunc(1, 4, 8)  # Calling with multiple positional arguments

# Returning multiple values (implicitly returns a tuple)
def myfunc():
    """
    Returns multiple values which are packed into a tuple.
    """
    return 1, 2, 3

print(myfunc())  # Output: (1, 2, 3)
x, y, z = myfunc()  # Unpacking the tuple into variables

# Combining collected arguments with keyword-only arguments
def myfunc(*args, a, b):
    """
    Shows combining collected positional arguments with keyword-only arguments.
    *args collects positional arguments, while 'a' and 'b' must be keyword arguments.
    """
    print(f"Positional args: {args}, Keyword args: a={a}, b={b}")

myfunc(1, 2, a=3, b=4)  # Positional then keyword arguments

# 10. COLLECTING KEYWORD ARGUMENTS
# Using **kwargs to collect keyword arguments into a dictionary
def myfunc(**kwargs):
    """
    Demonstrates collecting keyword arguments.
    **kwargs packs all keyword arguments into a dictionary.
    """
    print(kwargs)  # Dictionary of keyword arguments

myfunc(a=3, b=4)  # Calling with keyword arguments

# 11. MIXING ARGUMENT TYPES
# Combining all types of arguments
def myfunc(a, *b, **c):
    """
    Shows a function with a required positional argument,
    collected positional arguments, and collected keyword arguments.
    """
    print(f"Required arg: {a}, Collected positional args: {b}, Collected keyword args: {c}")

myfunc(1, 2, 3, c=4, d=5)  # Mixing argument types

# 12. UNPACKING ARGUMENTS
# Unpacking a tuple to pass as positional arguments
args = (1, 2, 3, 4)

def myfunc(a, b, c, d):
    """
    A function expecting four positional arguments.
    """
    print(a, b, c, d)

# myfunc(args)  # TypeError: too many positional arguments
myfunc(*args)  # Unpacking the tuple to pass as individual arguments


# Unpacking a dictionary to pass as keyword arguments
kwargs = {"a": 1, "b": 2, "c": 3, "d": 4}
myfunc(**kwargs)  # Unpacking the dictionary to pass as keyword arguments


# ==============================================================================
# ADDITIONAL NOTES
# ==============================================================================

"""
Key Points:

1. *args collects positional arguments into a tuple, useful when the number of arguments is unknown.
2. **kwargs collects keyword arguments into a dictionary, allowing flexible keyword parameter passing.
3. Mixing argument types requires attention to order: required positional, *args, then keyword-only or **kwargs.
4. Unpacking with * (for tuples) and ** (for dictionaries) allows using collections to supply arguments to functions.
5. Keyword-only arguments (after * in the parameter list) enforce clarity by requiring explicit naming of parameters.
6. Default values can be combined with collected arguments, but defaults cannot be set for *args or **kwargs directly.
7. When unpacking, the number and names of items must match the function's parameter list to avoid errors.
8. These features enable writing flexible, reusable functions that can handle varying input scenarios.
"""