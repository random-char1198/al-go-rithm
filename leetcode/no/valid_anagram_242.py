from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
class Solution1:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt1, cnt2 = Counter(s),Counter(t)
        return cnt1 & cnt2 == cnt1 and cnt1 & cnt2 == cnt2

