class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        while len(stones) > 1:
            stones.sort()
            y = stones[-1]
            x = stones[-2]
            if x <= y:
                if x == y:
                    stones.pop()
                    stones.pop()
                elif x != y:
                    tmp = y - x
                    stones.pop()
                    stones.pop()
                    stones.append(tmp)
        if not stones:
            stones.append(0)
        return stones[0]
