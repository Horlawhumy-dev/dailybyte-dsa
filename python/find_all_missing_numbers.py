

def find_all_missing_numbers(arr):
    """ [2, 3, 1, 8, 2, 3, 5, 1] """
    i = 0
    result = []

    while i < len(arr):
        num_index = arr[i] - 1

        if num_index != i:
            swap(arr, i, num_index)      
        i += 1


    for index, value in enumerate(arr):

        if value != index+1:
            result.append(index+1)

    return result
            

def swap(arr, start, end):

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp


print(find_all_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))