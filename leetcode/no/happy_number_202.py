class Solution:
    def isHappy(self, n: int) -> bool:
        s = set()
        while n not in s:
            s.add(n)
            tmp = 0
            for i in str(n):
                tmp += int(i) ** 2
            if tmp == 1:
                return True
            else:
                n = tmp
        return False


solution = Solution()
print(solution.isHappy(2))
