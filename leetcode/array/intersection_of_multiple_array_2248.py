from collections import Counter


class Solution:
    def intersection(self, nums: list[list[int]]) -> list[int]:
        res = None
        for i in range(len(nums)):
            cnt = Counter(nums[i])
            if res is None:
                res = cnt
            else:
                res &= cnt
        return list(res.elements())


s = Solution()
print(s.intersection([[3, 1, 2, 4, 5], [1, 2, 3, 4], [3, 4, 5, 6]]))
