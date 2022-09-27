class Solution:
    def toHex(self, num: int) -> str:
        dic = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'a', 11: 'b',
               12: 'c', 13: 'd', 14: 'e', 15: 'f'}
        if num == 0:
            return '0'
        if num < 0:
            num = (abs(num) ^ (2 ** 32 - 1)) + 1
            res = ''
            while num > 0:
                res = res + dic[num % 16]
                num = num // 16
            return res[::-1]
        else:
            print(dic)
            res = ''
            while num > 0:
                res = res + dic[num % 16]
                num = num // 16
            return res[::-1]


solution = Solution()
print(solution.toHex(-2))
