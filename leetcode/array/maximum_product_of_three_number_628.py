class Solution:
    def maximumProduct(self, nums: list[int]) -> int:
        nums = sorted(nums)
        print(nums)
        return max(nums[0] * nums[1] * nums[-1], nums[-1] * nums[-2] * nums[-3])
