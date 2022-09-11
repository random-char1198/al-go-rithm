class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:
        res = 0
        for i in range(1, len(timeSeries)):
            if timeSeries[i] - timeSeries[i - 1] < duration:
                res += (timeSeries[i] - timeSeries[i - 1])
            else:
                res += duration
        res += duration
        return res