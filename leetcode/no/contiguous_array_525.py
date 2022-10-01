class Solution:
    def findMaxLength(self, nums: list[int]) -> int:
        sub_sum = 0
        max_len = 0
        dic = {}
        for i in range(len(nums)):
            if nums[i] == 1:
                sub_sum += 1
            else:
                sub_sum -= 1
            if sub_sum == 0:
                max_len = max(max_len,i+1)
            if sub_sum in dic:
                max_len = max(max_len,i - dic[sub_sum])
            if sub_sum not in dic:
                dic[sub_sum] = i
        return max_len