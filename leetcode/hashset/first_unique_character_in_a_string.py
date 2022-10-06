from collections import Counter


class Solution:
    def firstUniqChar(self, s: str) -> int:
        cnt = Counter()
        print(cnt[s])
        for i in range(len(s)):
            cnt[s[i]] += 1
        print(cnt)