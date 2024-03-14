#! 30 MINS
# ! 1. Arrays
# Creating an array
my_array = [1, 2, 3, 4, 5]

# Accessing elements
print(my_array[0])  # Output: 1
print(my_array[2])  # Output: 3

# Modifying elements
my_array[1] = 10
print(my_array)  # Output: [1, 10, 3, 4, 5]

# Array length
print(len(my_array))  # Output: 5

# Iterating over an array
for element in my_array:
    print(element)

# ! More on arrays:
# List with elements
numbers = [1, 2, 3, 4, 5]
mixed_list = [1, 'apple', 3.14, True]

# ?Accessing elements:
fruits = ['apple', 'banana', 'cherry']

# Access by index
print(fruits[0])  # Output: 'apple'
print(fruits[2])  # Output: 'cherry'

# Access by negative index
print(fruits[-1])  # Output: 'cherry'

# Slicing (range of elements)
print(fruits[1:3])  # Output: ['banana', 'cherry']

# ?List operations:
# Length of a list
numbers = [1, 2, 3, 4, 5]
print(len(numbers))  # Output: 5

# Concatenate lists
list1 = [1, 2, 3]
list2 = [4, 5, 6]
new_list = list1 + list2
print(new_list)  # Output: [1, 2, 3, 4, 5, 6]

# Repeat a list
repeated_list = [1, 2] * 3
print(repeated_list)  # Output: [1, 2, 1, 2, 1, 2]

# Check if an element exists in a list
numbers = [1, 2, 3, 4, 5]
print(3 in numbers)  # Output: True
print(10 in numbers)  # Output: False

# ?List methods:
fruits = ['apple', 'banana', 'cherry']

# Append an element
fruits.append('orange')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'orange']

# Insert an element at a specific index
fruits.insert(1, 'mango')
print(fruits)  # Output: ['apple', 'mango', 'banana', 'cherry', 'orange']

# Remove an element by value
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'mango', 'cherry', 'orange']

# Remove an element by index
del fruits[1]
print(fruits)  # Output: ['apple', 'cherry', 'orange']

# Sort the list
numbers = [5, 2, 8, 1, 9]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 8, 9]

# ! 2. Stacks
# Creating a stack
stack = []

# Push (add) elements to the stack
stack.append(1)
stack.append(2)
stack.append(3)
print(stack)  # Output: [1, 2, 3]

# Pop (remove) elements from the stack
popped_element = stack.pop()
print(popped_element)  # Output: 3
print(stack)  # Output: [1, 2]

# Check if the stack is empty
print(len(stack) == 0) # Output: False