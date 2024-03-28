input_arr = [10,11,1,6,3,1,5,0]

def insertion_sort(arr):
    n = len(arr) # get the length of the array -> 5

    for i in range(1, n): # Loop through the array (1 till end - 5)
        key = arr[i]
        j = i - 1 # compare the current element with the left elements

        # this loop is for continuously comparing the 
        # current element with the left elements until it is on the correct spot
        while j >= 0 and key < arr[j]:
            # swap
            arr[j+1] = arr[j]
            j -= 1 # if the current element is less than the left element, 
                    # keep moving to the left until it is on the correct spot
        arr[j+1] = key # insert the current element to the correct spot
    return arr

sortedarr = insertion_sort(input_arr) 
print('sorted:', sortedarr)