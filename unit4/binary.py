# binary search

# input array
arr = [3,4,5,6,7,8,9]
target = 1

low = 0
high = len(arr) - 1

# loop 
result = False
while low <= high:
    # divide
    mid = (low + high) // 2 # this is the middle index (not the value of the arr)

    # compare the middle with the target
    if arr[mid] == target:
        result = True
        break

# compare and discard the half
    if target > arr[mid]:
        low = mid + 1
    else:
        high = mid - 1

if result == True:
    print('Found')
else:
    print("Not found")
