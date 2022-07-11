def selectSort(nums):
    for i in range(len(nums)):
        min_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[min_index]:
                min_index = j
        if min_index != i:
            tmp = nums[min_index]
            nums[min_index] = nums[i]
            nums[i] = tmp
    return nums


print(selectSort([231, 21, 1, 3, 6, 7, 6]))
