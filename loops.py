# loop over an array
fruits = ['a', 'b', 'c']

# loop through each evelement
# at each stage, if the element is 'c'
# print true
# for e in fruits: # 1.e = 'a', 2.e = 'b 3. e = 'c'
#     if e == 'c':
#         print('True from c')
#     if e == 'b':
#         print('True from b')




# # # Iterate over a string
# greeting = "Hello"
# for char in greeting:
#     print(char)
#     # Exercise: check if the string contains vowel




# Iterate over a range
# for i in range(5,14,2): #  5 - 13
#     print(i)






# Iterate over a range with step
# for i in range(0, 10, 2):
#     print(i)  # Output: 0 2 4 6 8


#! While Loops
# Basic while loop

count = 0
while count < 5:
 # print(count)
    count = count + 1 # Output: 0 1 2 3 4

# user input string is unknown
# print every char of the string
s = 'helloabc'
counter = 0
lenth_s = len(s)
print('coutner:', counter)
print('len s:', lenth_s)
# 0 , 1 , 2, 3, 
print('going in loop')
while counter < lenth_s:
    print('counter:', counter)
    char = s[counter]
    print(char)
    counter = counter + 1
    print('-----')
