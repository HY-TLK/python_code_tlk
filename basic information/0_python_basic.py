# Identifier Naming Rules
# - Must be meaningful
# - Can only contain letters, numbers, and underscores
# - Cannot start with a number
# - Cannot be a keyword
# - Case-sensitive

# Data Types
# Numeric Types
int_num = 10                  # Integer type
float_num = 10.5              # Float type
complex_num = 3 + 4j          # Complex number type
bool_val = True               # Boolean type

# Accurate Floating-Point Calculation
import decimal
a = decimal.Decimal('0.1')
b = decimal.Decimal('0.2')
print(a + b)  # Outputs 0.3

# Boolean Value Evaluation
false_values = [None, False, 0, 0.0, '', (), [], {}, set(), range(0)]
for val in false_values:
    print(bool(val))  # All output False

# Logical Operators
print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True)        # Output: False

# Operator Precedence
# not > and > or

# Assignment Operators
a = 5
a += 3  # Equivalent to a = a + 3
a -= 2  # Equivalent to a = a - 2
a *= 4  # Equivalent to a = a * 4
a /= 2  # Equivalent to a = a / 2
a //= 1 # Equivalent to a = a // 1
a %= 3  # Equivalent to a = a % 3
a **= 2 # Equivalent to a = a ** 2

# String Formatting
# Using % formatting
name = "Harry"
age = 19
print("My name is %s, I am %d years old" % (name, age))
print("Float value: %f" % 3.1415926)       # Default six decimal places
print("Formatted float: %.2f" % 3.1415926) # Keep two decimal places

# Using .format() method
print("Hello, {}".format("World"))
print("My name is {}, I am {} years old".format(name, age))
print("{0} is {1} years old, {0} is learning Python".format(name, age))

# Using f-string
print(f"My name is {name}, I am {age} years old")

# Conditional Statements (if)
x = 10
if x > 0:
    print("x is positive")
elif x == 0:
    print("x is zero")
else:
    print("x is negative")

# Using if as an Expression
result = "Even" if x % 2 == 0 else "Odd"
print(result)

# Loop Statements
# while loop
count = 0
while count < 5:
    print(count)
    count += 1
else:
    print("Loop ended")

# break and continue usage
while True:
    num = int(input("Enter a number (negative to exit): "))
    if num < 0:
        break
    if num % 2 == 0:
        continue
    print(f"Odd number: {num}")

# for loop
for i in range(5):  # 0 to 4
    print(i)

for i in range(2, 8, 2):  # Start from 2, up to 8 (exclusive), step of 2
    print(i)

# Nested loops - Multiplication Table
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j}x{i}={i*j}", end="\t")
    print()

# Finding Prime Numbers under 10
for num in range(2, 10):
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        print(num)