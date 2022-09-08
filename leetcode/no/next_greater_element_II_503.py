class Solution:
    def nextGreaterElements(self, nums):
        res, stack = [], []
        res = [-1] * len(nums)
        for i in range(2 * len(nums)):
            index = i % len(nums)
            # 5 % 7 = 5 if len(nums) == 7
            # 7 % 7 = 0 if len(nums) == 7
            # we have chance to iterate nums the second time.
            while stack and nums[stack[-1]] < nums[index]:
                res[stack.pop()] = nums[index]
            if i < len(nums):
                stack.append(i)
        return res

