#! 30 MINS
#! For Loops
# Iterate over a list
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
 print(fruit)

# Iterate over a string
greeting = "Hello"
for char in greeting:
 print(char)

# Iterate over a range
for i in range(5):
 print(i) # Output: 0 1 2 3 4

# Iterate over a range with step
for i in range(0, 10, 2):
 print(i) # Output: 0 2 4 6 8

#! While Loops
# Basic while loop
count = 0
while count < 5:
 print(count)
 count += 1 # Output: 0 1 2 3 4

# Break statement
number = 0
while True:
 if number == 5:
  break
 print(number)
 number += 1 # Output: 0 1 2 3 4

# Continue statement
for i in range(10):
 if i % 2 == 0:
  continue
 print(i) # Output: 1 3 5 7 9

#! Nested Loops
# Nested for loop
for i in range(3):
 for j in range(3):
  print(f"({i}, {j})")

# Output:
# (0, 0) (0, 1) (0, 2)
# (1, 0) (1, 1) (1, 2)
# (2, 0) (2, 1) (2, 2)

# Nested while loop
i = 0
while i < 3:
 j = 0
 while j < 3:
   print(f"({i}, {j})")
   j+=1
   j+=1
   i+=1