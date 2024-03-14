# loop over an array
fruits = ['a', 'b', 'c']

# loop through each evelement
# at each stage, if the element is 'a'
# print true
for e in fruits: # 1.e = 'a', 2.e = 'b 3. e = 'c'
    if e == 'c':
        print('True from c')
    if e == 'b':
        print('True from b')

# # Iterate over a string
greeting = "Hello"
for char in greeting:
    print(char)
# Exercise: check if the string contains vowel
    
#iterate over a range
    for i in range(9):#0 - 8
        print(i) #output: 5 6 7 8 9 10 11 12 13
        val = i + 5
        print(val)
