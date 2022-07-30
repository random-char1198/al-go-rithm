class Solution:
    def sortColors(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p0, p2 = 0, len(nums) - 1
        left = 0
        while left <= p2:
            if nums[left] == 2:
                nums[left], nums[p2] = nums[p2], nums[left]
                p2 -= 1
            elif nums[left] == 0:
                nums[left], nums[p0] = nums[p0], nums[left]
                left += 1
                p0 += 1
            elif nums[left] == 1:
                left += 1

