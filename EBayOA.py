#from my assessment at eBay
#State Changes
def count_state_changes(arr):
    if not arr:
        return 0

    changes = 0
    for i in range(1, len(arr)):
        if arr[i].upper() != arr[i - 1].upper():
            changes += 1

    return changes
#I got this question by 300/300


# Find the leftmost non-zero value, substract from all values until you find one less than the non-zero value, then add the non-zero to the return value, repeat until the array is equal to 0.  Return the ret value
def prefix_reduce(nums):
    nums = nums[:]  # copy
    ret = 0
    n = len(nums)

    while True:
        i = 0
        while i < n and nums[i] == 0:
            i += 1
        if i == n:
            break

        x = nums[i]
        ret += x

        j = i
        while j < n and nums[j] >= x:
            nums[j] -= x
            j += 1

    return ret
    #I got this question 160/300
