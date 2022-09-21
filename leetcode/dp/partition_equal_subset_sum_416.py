class Solution:
    def canPartition(self, nums) -> bool:
        if sum(nums) % 2 != 0:
            return False
        else:

