class Solution:
    def wordBreak(self, s: str, wordDict: list[str]) -> bool:
        length = len(s)
        dp = [False] * (length + 1)
        dp[0] = True
        for i in range(length):
            for j in range(i + 1, length + 1):
                if dp[i] and s[i:j] in wordDict:
                    dp[j] = True
                    print(i, j, s[i:j], True)
                else:
                    print(s[i:j])
        return dp[-1]


s = Solution()
print(s.wordBreak("leetcode", ['leet', 'code']))
