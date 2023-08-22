

def corrupt_pair(nums: list):
    """ [3, 1, 2, 5, 2] """

    result_nums = []

    i = 0

    while i < len(nums):
        if nums[i] != nums[nums[i]-1]:
            swap(nums, i, nums[i]-1)
        else:
            i+=1

    for i in range(len(nums)):

        if nums[i] != i+1:
            result_nums.append(i+1)
            result_nums.append(nums[i])

    return result_nums

def swap(nums, start, end):

    temp = nums[start]
    nums[start] = nums[end]
    nums[end] = temp

print(corrupt_pair([3, 1, 2, 3, 6, 4]))