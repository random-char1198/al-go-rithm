class Solution:
    def maxAscendingSum(self, nums: list[int]) -> int:
        res = cur = 0
        for i in range(len(nums)):
            if i == 0 or nums[i] > nums[i-1]:
                cur += nums[i]
                res = max(res,cur)
            else:
                cur = nums[i]
        return res

