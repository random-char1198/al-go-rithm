class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0
        for i in range(len(columnTitle)):
            ch = ord(columnTitle[i]) - 65 + 1
            res = res * 26 + ch
        return res