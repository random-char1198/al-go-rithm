class Solution:
    def arrayPairSum(self, nums) -> int:
        res = 0
        nums = sorted(nums) # n log n
        for i in range(len(nums)):
            if i % 2 == 0:
                res += nums[i]
        return res

