def two_sum1(nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                target_val = nums[i] + nums[j]
                if target_val == target:
                    return [i,j]
        return []
    #O(n^2)

def two_sum3(nums,target):
    dict = {}
    for index, item in enumerate(nums):
        left =  target - item # 1. 12 - 2 = 7
        if left in dict:
            return [dict[left],index]
        else:
            dict[item] = index
        
print(two_sum3([2,7,11,15],9))
'''
Store targer value as key, i as index {vlaue:index},
When we are trying to find if the index of the value is in the dictionary, we can just return it.
'''
