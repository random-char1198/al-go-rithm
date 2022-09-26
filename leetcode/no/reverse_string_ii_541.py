class Solution:
    def reverseStr(self, s: str, k: int):
        t = list(s)
        for i in range(0, len(t), 2 * k):
            t[i:i + k] = reversed(t[i:i + k])
            # [1,2,3,4,5]
            # t[0:2] = [1,2]

        return "".join(t)


solution = Solution()
print(solution.reverseStr("abcdefg", 2))
