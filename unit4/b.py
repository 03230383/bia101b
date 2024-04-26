input_str = "((()"

floor_index = 0 #? variable to keep track of the ans
for i in input_str: #! go through each character 
    if i == "(": #? if ( add one to the answer
        floor_index = floor_index + 1
    if i == ")": #? if ) sub one to the answer
        floor_index = floor_index - 1
# print the final answer
print('the final floor is', floor_index)
stack = []
for char in input_str:
    if char == "(":
        stack.append(char)
    if char == ")":
        stack .pop()
length = len(stack)
print("length",length) 
if length == 0:
    print("True")
else:
    print("False")