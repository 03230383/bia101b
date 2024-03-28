input_arr = [6,3,1,5,9]


def bubble_sort(arr):
    n = len(arr)

    for i in range(n): # 0,1,2,3,4,5
        print('before first for loop')
        for k in range(0, (n-1)):
            print('inside first for loop')
            print()
            element = arr[k]
            elementright = arr[k+1]
            print('elementright:', element)
            print('element:', elementright)
            print('============================')
            # swap
            if element > elementright:
                arr[k] = elementright
                arr[k+1] = element

bubble_sort(input_arr)

