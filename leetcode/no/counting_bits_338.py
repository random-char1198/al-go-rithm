class Solution:
    def countBits(self, n: int):
        res = []
        for i in range(n + 1):
            bit = bin(i)
            res.append(bit.count('1'))
        return res
