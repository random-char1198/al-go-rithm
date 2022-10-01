class Solution:
    def divideString(self, s: str, k: int, fill: str) -> list[str]:
        res = []
        for i in range(0, len(s), k):
            res.append(s[i:i + k])
            # print(s[i:i+k])
        if len(res[-1]) < k:
            length = k - len(res[-1])
            res[-1] += length * fill
        return res
