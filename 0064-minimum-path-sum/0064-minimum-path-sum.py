class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]        
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if (i, j) == (m - 1, n - 1): 
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(
                        dp[i + 1][j] if i + 1 < m else inf, 
                        dp[i][j + 1] if j + 1 < n else inf
                    )

        return dp[0][0]
