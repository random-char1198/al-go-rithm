class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        res = 0
        for i in range(len(jewels)):
            stones = stones.replace(jewels[i],"1")
        for ch in stones:
            res += 1 if ch == "1" else 0
        return res
