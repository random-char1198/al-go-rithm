from collections import Counter

class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter()
        for c in s:
            cnt[c] += 1

        for i in range(len(s)):
            if cnt[s[i]] == 1:
                return i
        return -1
