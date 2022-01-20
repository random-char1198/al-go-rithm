def max_subarray(nums):
    curr_max = global_max = nums[0]
    # since we already picked the first item in the list as our global and curr max. So out iteration wil start with the second item.
    for i in range(1, len(nums)):
        curr_max = max(nums[i], nums[i] + curr_max)
        if curr_max > global_max:
            global_max = curr_max
    return global_max


print(max_subarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
print(max_subarray([1]))
print(max_subarray([5, 4, -1, 7, 8]))
