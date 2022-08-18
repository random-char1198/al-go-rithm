class Solution:
    def coinChange(self, coins, amount: int) -> int:
        dp = [0] * (amount + 1)

        for i in range(1, amount + 1):
            min_val = float('inf')
            for j in range(len(coins)):
                if i - coins[j] >= 0:
                    min_val = min(min_val, dp[i - coins[j]] + 1)
            dp[i] = min_val

        if dp[amount] == float('inf'):
            return -1
        else:
            return dp[amount]


solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
