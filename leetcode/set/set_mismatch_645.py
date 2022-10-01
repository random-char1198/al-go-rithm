from collections import defaultdict
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        dic = defaultdict()
        res = [-1] * 2
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = 1
            else:
                dic[nums[i]] += 1
        # print(dic)
        for i in range(1,len(nums)+1,1):
            if i not in dic:
                res[1] = i
            elif dic[i] == 2:
                res[0] = i
        return res
