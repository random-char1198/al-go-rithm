# 1784
class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        pointer = 0
        while pointer < len(s) and s[pointer] == '1':
            pointer += 1
        while pointer < len(s) and s[pointer] == '0':
            pointer += 1
        return pointer == len(s)