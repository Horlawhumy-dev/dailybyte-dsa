

def find_missing_number(arr):

    for i in range(len(arr)):

        if i in arr:
            continue
        else:
            return i

print(find_missing_number([1, 2, 4, 3]))