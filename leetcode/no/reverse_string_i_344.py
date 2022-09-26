class Solution:
    def reverseString(self, s: list[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        left, right = 0, len(s) - 1
        t = list(s)
        while left <= right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
        # s = "".join(t)
        # print(t)
        print(s)


solution = Solution()
solution.reverseString(['h', 'e', 'l', 'l', 'o'])
