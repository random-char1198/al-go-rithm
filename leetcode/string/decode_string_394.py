class Solution:
    def decodeString(self, s: str) -> str:
        # >> > a = []
        # >> > a.append(1)
        # >> > a.append(2)
        # >> > a.append(3)
        # >> > a
        # [1, 2, 3]
        # >> > a.pop()
        # 3
        # >> > a
        # [1, 2]
        # >> >
        stack = []
        num = 0
        res = ""
        for ch in s:
            if ch.isdigit():
                num = num * 10 + int(ch)
            elif ch == "[":
                stack.append((num, res))
                # reset
                res, num = "", 0
            elif ch == "]":
                right = stack.pop()
                res = right[0] + res * right[1]
            else:
                res += ch
            return res
