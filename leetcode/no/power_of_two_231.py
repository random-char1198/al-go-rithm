class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        if n == 0:
            return False
        else:
            if n % 2 == 0:
                # remainder == 0 is the key to this question.
                return self.isPowerOfTwo(n // 2)
            else:
                return False


solution = Solution()
print(solution.isPowerOfTwo(12))
