# objective: a calculator application made using
# variables and if statements

# steps
# 1. get unput from the user
# 2. do calculation based on user input
# 3. give output to the user

print('* for multiplication')
print('+ for addition')
print('- for subtraction')
print('/ for division')

whatUserTyped = input()

print('User typed:', whatUserTyped)
print('user input-type', type(whatUserTyped))

if whatUserTyped == "+":
    print('Doing Addition')
    print('doing more addition')

if whatUserTyped == "-":
    print('Doing subtraction')
    print('doing more subtraction')