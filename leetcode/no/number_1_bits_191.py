class Solution:
    def hammingWeight(self, n: int) -> int:
        bit = bin(n)
        res = 0
        for i in range(2, len(bit)):
            if int(bit[i]) & 1 == 1:
                res += 1
        return res
