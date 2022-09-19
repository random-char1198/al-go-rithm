class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        cap_cnt = 0
        for i in range(len(word)):
            if ord(word[i]) <= 90:
                cap_cnt += 1
        if cap_cnt == len(word):
            return True
        elif cap_cnt == 0:
            return True
        elif cap_cnt == 1 and ord(word[0]) <= 90:
            return True
        else:
            return False

solution = Solution()
print(solution.detectCapitalUse("USA"))
print(solution.detectCapitalUse("leetcode"))
print(solution.detectCapitalUse("Google"))
print(solution.detectCapitalUse("FlaG"))
