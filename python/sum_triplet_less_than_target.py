

def sum_triplet_less_than_target(arr, target):
    arr = sorted(arr)
    array_len = len(arr)

    triplets_arr = []

    for i in range(array_len-2):
        left = i + 1
        right = array_len - 1
        while left < right:

            tripletSum = arr[i] + arr[left] + arr[right]

            if tripletSum < target:
                triplets_arr.append([arr[i], arr[left], arr[right]])
                left += 1
            else:
                right -= 1

        

    return triplets_arr

print(sum_triplet_less_than_target([-1, 2, 0, 3], 3))

