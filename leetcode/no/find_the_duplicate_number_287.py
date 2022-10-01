from collections import defaultdict

class Solution:
    def findDuplicate(self, nums: list[int]) -> int:
        dic = defaultdict()
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        for i in range(len(dic)):
            if dic[i] == 2:
                return dic[i]
