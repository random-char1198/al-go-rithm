class Solution:
    def maxProfit(self, prices) -> int:
        if len(prices) == 1:
            return 0
        min_price, max_profit = prices[0], 0
        for i in range(len(prices)):
            min_price = min(prices[i], min_price)
            max_profit = max(max_profit, prices[i] - min_price)
        return max_profit


solution = Solution()
print(solution.maxProfit([7, 1, 5, 3, 6, 4]))
