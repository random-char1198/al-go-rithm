import math


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        # res = 1
        # for i in range(2, num + 1):
        #     if num % i == 0 and i != num:
        #         res += i
        # # print(res)
        # return res == num
        if num == 1:
            return False
        res = 1
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                res += (i + num // i)
                # get remainder and quotient
        # print(res)

        return res == num
