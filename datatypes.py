#creation of array
array1 = [1,2,3, "thimphu", 2.5]

#retriveing
element1 = array1[0]
element2 = array1[4]
last_element = array1[-5]
#print(last_element)

#modifying elements
#array1[0] = 10

#getting number of elements in an array
no_of_elements = len(array1)
#print(no_of_elements)

#slicing
elements = array1[0:3]
#print(elements)

arr1 = [1,10]
arr2 = ['thimphu', 'wangdue']

#number_to_check = 2
#result = number_to_check in arr1
#print('result is', result)

arr3 = arr1 + arr2
#print(arr3)

#arr_variable = [1,2,3]
#arr_variable.append(4)
#print(arr_variable)

#insert at a specific index
#arr_variable.insert(1,10) #[1,10,3,2,4]
#arr_variable.sort()
#print(arr_variable)

stack_var = []
#adding to stack
stack_var.append(4)
stack_var.append(2)
stack_var.append(9)
stack_var.append(1) #4,2,9,1
print('after appending', stack_var)
stack_var.pop()
print('after popping', stack_var)
