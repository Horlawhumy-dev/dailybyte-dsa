

def cyclic_sort(arr):
    """ T[n] -> O(n), S[n] -> O(1) where arr is 1 -> n"""
    for i in range(len(arr)):
        num_index = arr[i]-1

        if num_index == i:
            continue
        else:
            swap(arr, num_index, i)

    return arr


def swap(arr, start, end):

    temp = arr[start]
    arr[start] = arr[end]
    arr[end] = temp

print(cyclic_sort([4, 0, 3, 1]))