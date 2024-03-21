#* 40 MINS
#! Simple function
def greet():
    print("Hello, World!")

greet() # Output: Hello, World!

# Function with parameters
def add_numbers(a, b):
    sum = a + b
    return sum

result = add_numbers(3, 5)
print(result) # Output: 8

#! Deafult Params value:
def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice") # Output: Hello, Alice!
greet("Bob", "Hi") # Output: Hi, Bob!

#! Nested Functions:
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func

#! - READ args in functions
# *args (Non-Keyword Arguments)
def print_numbers(*args):
    for arg in args:
        print(arg)

print_numbers(1, 2, 3) # Output: 1 2 3
# **kwargs (Keyword Arguments)
def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_info(name="Alice", age=25, city="New York")
# Output:
# name: Alice
# age: 25
# city: New York

#! Recursive Functions
# Factorial
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5)) # Output: 120

#! Doc Strings:
def greet(name):
    """
    This function greets the person with the given name.

    Args:
    name (str): The name of the person to greet.

 Returns:
str: The greeting message.
"""


print(greet("Alice")) # Output: Hello, Alice!
print(greet.__doc__) # Print the docstring

#! Annotations:
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

result = multiply(3, 5)
print(result) # Output: 15

#! Higher Order Functions:
def apply_operation(func, x, y):
    result = func(x, y)
    return result

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b

print(apply_operation(add, 3, 4)) # Output: 7
print(apply_operation(multiply, 3, 4)) # Output: 12

add_with_5 = outer_func(5)
print(add_with_5(3)) # Output: 8
print(add_with_5(10)) # Output: 15
