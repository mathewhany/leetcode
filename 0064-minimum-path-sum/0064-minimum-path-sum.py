class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        dp = [0 for _ in range(n)]
        
        for i in range(m):
            for j in range(n):
                if (i, j) == (0, 0): 
                    dp[j] = grid[i][j]
                else:
                    dp[j] = grid[i][j] + min(
                        dp[j] if i - 1 >= 0 else inf, 
                        dp[j - 1] if j - 1 >= 0 else inf
                    )

        return dp[-1]
