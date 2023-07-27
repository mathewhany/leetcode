class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [[0 for _ in range(n + 1)] for _ in range(m + 1)]

        dp[0][0] = 1

        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0): continue

                top = dp[i - 1][j] if i - 1 >= 0 else 0
                left = dp[i][j - 1] if j - 1 >= 0 else 0
                
                dp[i][j] = top + left

        return dp[m - 1][n - 1]
            