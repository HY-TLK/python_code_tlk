# Local Scope
def myfunc():
    local_x = 520  # local_x is a local variable
    print(local_x)  # Output: 520

myfunc()
# print(local_x)  # Error: local_x is not defined outside the function

# Global Scope
global_x = 880  # global_x is a global variable

def myfunc():
    print(global_x)  # Access the global variable global_x

myfunc()  # Output: 880

# Local variable shadows global variable
def myfunc():
    local_x = 520  # Local variable local_x shadows the global global_x
    print(local_x)  # Output: 520

myfunc()

# The global Statement
def myfunc():
    global global_x  # Declare global_x as a global variable
    global_x = 1  # Modify the global variable global_x
    print(global_x)  # Output: 1

myfunc()
print(global_x)  # Output: 1

# Nested Functions
def funA():
    enclosing_x = 520  # enclosing_x is in the scope of funA

    def funB():
        local_x = 880  # local_x is a local variable in funB
        print("funB: ", local_x)  # Output: funB:  880

    funB()
    print("funA:", enclosing_x)  # Output: funA: 520

funA()

# The nonlocal Statement
def outter(initial_value):
    enclosing_y = initial_value  # enclosing_y is in the scope of outter

    def inner():
        nonlocal enclosing_y  # Declare enclosing_y as nonlocal
        enclosing_y = enclosing_y * 3  # Modify the nonlocal variable enclosing_y

    inner()  # Call inner() to modify enclosing_y
    enclosing_y += 2
    return enclosing_y

print(outter(3))  # Output: 11 (3 * 3 + 2)

# LEGB Rule: Local -> Enclosing -> Global -> Built-in
# Python follows the LEGB rule for variable lookup:
# 1. Local scope (inside the current function)
# 2. Enclosing scope (nested functions)
# 3. Global scope (module level)
# 4. Built-in scope (Python's built-in functions and variables)