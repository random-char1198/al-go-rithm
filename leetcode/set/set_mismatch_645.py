class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        res = []
        for i in range(1, len(nums) - 1, 2):
            if nums[i] == nums[i - 1]:
                res += nums[i]
        return res


s = Solution()
print(s.findErrorNums([1, 2, 2, 4]))
