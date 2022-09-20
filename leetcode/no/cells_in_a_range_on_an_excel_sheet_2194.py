class Solution:
    def cellsInRange(self, s: str):
        res = []
        for i in range(ord(s[0]), ord(s[3]) + 1):
            for j in range(int(s[1]), int(s[4]) + 1):
                # print(i,j)
                res.append(chr(i) + str(j))
                # print(chr(i)+str(j+1))
        return res


solution = Solution()
solution.cellsInRange('A1:F1')
solution.cellsInRange("U7:X9")
