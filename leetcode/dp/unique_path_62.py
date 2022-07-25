class Solution:
    def uniquePaths(self, m: int, n: int):
        # f = [[1] * n] + [[1] + [0] * (n - 1) for _ in range(m - 1)]
        # print(f)
        dp = []
        for i in range(m):
            nested = []
            for j in range(n):
                if i == 0 or j == 0:
                    nested.append(1)
                else:
                    nested.append(0)

            dp.append(nested)
        # print(dp)
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        # print(dp)
        return dp[-1][-1]

solution = Solution()
solution.uniquePaths(3, 7)
