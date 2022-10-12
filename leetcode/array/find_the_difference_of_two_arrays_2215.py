from collections import Counter


class Solution:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        res = []
        shared_items = Counter(nums2) & Counter(nums1)
        shared_items_list = list(shared_items.elements())
        for i in range(len(shared_items_list)):
            while shared_items_list[i] in nums2:
                nums2.remove(shared_items_list[i])
            while shared_items_list[i] in nums1:
                nums1.remove(shared_items_list[i])
        res.append(list(set(nums1)))
        res.append(list(set(nums2)))
        return res


class Solution2:
    def findDifference(self, nums1: list[int], nums2: list[int]) -> list[list[int]]:
        ans = []
        cc1 = list(set(nums1) - set(nums2))
        cc2 = list(set(nums2) - set(nums1))
        ans.append(cc1)
        ans.append(cc2)
        return ans


s = Solution()
print(s.findDifference([1, 2, 3], [2, 4, 6]))
