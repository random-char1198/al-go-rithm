from collections import Counter


class Solution:
    def repeatedCharacter(self, s: str) -> str:
        cnt = Counter()
        for ch in s:
            cnt[ch] += 1
            if cnt[ch] == 2:
                return ch


s = Solution()
print(s.repeatedCharacter("abccbaacz"))
