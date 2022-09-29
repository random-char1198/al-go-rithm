class Solution:
    def distributeCandies(self, candyType: list[int]) -> int:
        s = set()
        for i in range(len(candyType)):
            if candyType[i] not in s:
                s.add(candyType[i])
        ate_len = len(candyType) / 2  # 4
        if ate_len < len(s):
            return int(ate_len)
        else:
            return len(s)
        # else
        # return min(len(set(candyType)), len(candyType) // 2)
