class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        occur = [0] * 26
        for i in range(len(magazine)):
            occur[ord(magazine[i]) - ord('a')] += 1
        for i in range(len(ransomNote)):
            occur[ord(ransomNote[i]) - ord('a')] -= 1

        for i in range(len(occur)):
            if occur[i] < 0:
                return False
        return True


s = Solution()
print(s.canConstruct("aa", "aab"))
