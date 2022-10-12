from collections import Counter


class Solution:
    def intersect(self, nums1: list[int], nums2: list[int]) -> list[int]:
        intersect_len = 0
        res, short, longer = [], [], []
        if len(nums1) > len(nums2):
            intersect_len = len(nums2)
            short = nums2[:]
            longer = nums1[:]
        else:
            intersect_len = len(nums1)
            short = nums1[:]
            longer = nums2[:]
        cnt_longer, cnt_short = Counter(short), Counter(longer)
        print(cnt_longer)
        for i in range(intersect_len):
            if short[i] in longer and cnt_longer[short[i]] > 0 and cnt_short[short[i]] > 0:
                res.append(short[i])
                cnt_short[short[i]] -= 1
                cnt_longer[short[i]] -= 1
        return res
