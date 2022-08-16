class Solution:
    def fizzBuzz(self, n: int) -> [str]:
        res = []
        for i in range(1, n + 1):
            print(i)
            if i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuss")
            elif i % 3 == 0:
                res.append("Fizz")
            elif i % 5 == 0:
                res.append("Buss")
            else:
                res.append(str(i))
        return res


solution = Solution()
print(solution.fizzBuzz(5))
