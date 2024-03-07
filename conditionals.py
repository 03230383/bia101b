# objective: a calculator application made using
# variables and if statements

# steps
# 1. get unput from the user
# 2. do calculation based on user input
# 2.1 check what string did user typed
# 2.2 if user string == *then do multiplication and so on
# 3. give output to the user

print('* for multiplication')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

#print('User typed:', whatUserTyped)
#print('user input-type', type(whatUserTyped))

print('-------------------')
if whatUserTyped == "+":
    print('Doing Addition')
    if 'a' == 'b':
        print('a is not b')
    if 'b' == 'b':
        print('b is b')

print('doing more addition')

if whatUserTyped == "-":
    print('Doing Subtraction')
    print('doing more subtraction')