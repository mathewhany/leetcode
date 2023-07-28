class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [[0 for _ in range(n)] for _ in range(m)]        
        
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0): 
                    dp[i][j] = grid[i][j]
                else:
                    dp[i][j] = grid[i][j] + min(
                        dp[i - 1][j] if i - 1 >= 0 else inf, 
                        dp[i][j - 1] if j - 1 >= 0 else inf
                    )

        return dp[-1][-1]
