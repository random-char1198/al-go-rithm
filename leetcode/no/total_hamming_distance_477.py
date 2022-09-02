class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        res = 0
        for i in range(30):
            count = 0
            for num in nums:
                count += (num >> i) & 1
            res += count * (len(nums) - count)
        return res
