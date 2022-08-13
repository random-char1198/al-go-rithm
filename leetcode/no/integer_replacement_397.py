class Solution:
    def integerReplacement(self, n: int) -> int:
        count = 0
        return self.dg(count, n)

    def dg(self, count, n):
        if n == 1:
            return n
        if n % 2 == 0:
            # even
            return self.dg(count + 1, n / 2)
        else:
            return min(self.dg(count + 1, n + 1), self.dg(count + 1, n - 1))
