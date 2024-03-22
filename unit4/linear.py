# searching
# sorting

# Problem 1
# input
user_input = [1,2,3,4,5,6,7,8,9,10]

# check to see if a certain number exist in the iser input array
n = 14
# linear
result = False # a variable to keep track of your answer
for i in user_input:
    if i == n:
        result = True
if result == True:
    print('found')
else:
    print('not found')


# if else, for loops, print, calculations (+,-)