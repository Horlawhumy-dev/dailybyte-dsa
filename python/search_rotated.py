def search(arr, target) :
    # Write your code here.
    k, m = 0, 0
    for i in range(len(arr)-1):
        if arr[i+1] < arr[i]:
            k = b_search(arr[:i+1],target)
            m = b_search(arr[i+1:], target)
            break
            
    return k if k >= 0 else m


def b_search(arr, target):

    i , j = 0, len(arr)-1

    while i <= j:

        mid = (j+i) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:

            i = mid + 1
        else:
            j  = mid - 1
            
    return -1
print(search([4,5,6,7,0,1,2], 0))