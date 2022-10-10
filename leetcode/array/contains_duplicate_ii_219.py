class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if abs(dic[nums[i]] - i) <= k:
                    return True
                else:
                    dic[nums[i]] = i
        return False
