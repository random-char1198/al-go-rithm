class Solution:
    def checkRecord(self, s: str) -> bool:
        cons = 0

        for i in range(len(s)):
            if s[i] == 'L':
                cons += 1
                if cons >= 3:
                    return False
            else:
                cons = 0
        if s.count('A') > 1:
            return False
        return True
