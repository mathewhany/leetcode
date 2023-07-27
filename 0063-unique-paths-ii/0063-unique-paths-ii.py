class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                elif (i, j) == (0, 0):
                    dp[i][j] = 1
                else:
                    top = dp[i - 1][j] if i - 1 >= 0 else 0
                    left = dp[i][j - 1] if j - 1 >= 0 else 0
                    dp[i][j] = top + left

        return dp[m - 1][n - 1]