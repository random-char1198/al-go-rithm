class Solution:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        c = set(nums)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in c:
                res.append(i)
        return res


class Solution2:
    def findDisappearedNumbers(self, nums: list[int]) -> list[int]:
        res = []
        for index, item in enumerate(nums):
            if nums[abs(item) - 1] > 0:
                nums[abs(item) - 1] *= -1
        # [1,n]
        for i in range(len(nums)):
            if nums[i + 1] > 0:
                res.append(i + 1)
        return res
