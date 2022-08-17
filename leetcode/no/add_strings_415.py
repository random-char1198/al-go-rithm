class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        l1, l2, carry = len(num1), len(num2), 0
        num1 = num1[::-1]
        num2 = num2[::-1]
        # reverse the num
        res = []
        for i in range(max(l1, l2)):
            x, y = 0, 0
            if i >= l1:
                x = 0
            else:
                x = ord(num1[i]) - ord('0')
            if i >= l2:
                y = 0
            else:
                y = ord(num2[i]) - ord('0')
            sum_of = x + y + carry
            res.append(sum_of % 10)
            carry = sum_of // 10
        if carry != 0:
            res.append(carry)
        return ''.join(map(str, res[::-1]))


solution = Solution()
print(solution.addStrings('456', '77'))
