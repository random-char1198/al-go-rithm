class Solution:
    def convertToBase7(self, num: int) -> str:
        res = ""
        if num < 0:
            num = abs(num)
            while num > 0:
                remainder = num % 7
                num = num // 7
                res += str(remainder)
            return "-" + res[::-1]

        elif num > 0:
            while num > 0:
                remainder = num % 7
                num = num // 7
                res += str(remainder)
            return res
        else:
            return "0"


solution = Solution()
print(solution.convertToBase7(-7))
