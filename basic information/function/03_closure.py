# A closure is a function object that has access to variables from its scope even when the function is used outside that scope.

# Simple closure example
def outer_func():
    message = "Hello"  # Variable in the outer function's scope

    def inner_func():
        print(message)  # Inner function accesses the outer function's variable

    return inner_func  # Return the inner function

my_func = outer_func()  # Call the outer function to get a closure
my_func()  # Output: Hello

# Using a closure to create a counter
def create_counter():
    count = 0  # Variable to maintain state in the outer function

    def counter():
        nonlocal count  # Declare the use of the outer function's variable
        count += 1
        return count

    return counter

counter_a = create_counter()  # Create the first counter
print(counter_a())  # Output: 1
print(counter_a())  # Output: 2

counter_b = create_counter()  # Create the second counter
print(counter_b())  # Output: 1
print(counter_a())  # Output: 3

# Using a closure to create a multiplier with a parameter
def make_multiplier(n):
    def multiplier(x):
        return x * n
    return multiplier

times3 = make_multiplier(3)  # Create a closure that multiplies by 3
times5 = make_multiplier(5)  # Create a closure that multiplies by 5

print(times3(4))  # Output: 12
print(times5(4))  # Output: 20

# Complex closure example with multiple enclosed variables
def create_complex_closure(base_value):
    factor = 2

    def complex_func(n):
        nonlocal factor
        result = base_value + n * factor
        factor += 1
        return result

    return complex_func

closure_example = create_complex_closure(10)
print(closure_example(3))  # Output: 10 + 3*2 = 16
print(closure_example(3))  # Output: 10 + 3*3 = 19 (factor is now 3)

# Using closures to simulate class behavior
def create_account(initial_balance):
    balance = initial_balance

    def deposit(amount):
        nonlocal balance
        balance += amount
        return balance

    def withdraw(amount):
        nonlocal balance
        if amount <= balance:
            balance -= amount
            return balance
        else:
            return "Insufficient funds"

    return deposit, withdraw

deposit_func, withdraw_func = create_account(100)
print(deposit_func(50))   # Output: 150
print(withdraw_func(30))  # Output: 120
print(withdraw_func(200)) # Output: Insufficient funds