class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        if columnNumber <= 26:
            return chr(columnNumber - 1 + ord('A'))
        else:
            res = ""
            # > 26
            while columnNumber > 0:
                columnNumber -= 1
                res += chr(columnNumber % 26 + ord('A'))
                columnNumber = columnNumber // 26
            return res[::-1]


solution = Solution()
solution.convertToTitle(701)
