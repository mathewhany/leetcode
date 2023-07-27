class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n - 1, -1, -1):
            for i in range(m - 1, -1, -1):
                if obstacleGrid[i][j] == 1: 
                    dp[i][j] = 0
                elif (i, j) == (m - 1, n - 1):
                    dp[i][j] = 1
                else:
                    bottom = dp[i + 1][j] if i + 1 < m else 0
                    right = dp[i][j + 1] if j + 1 < n else 0
                    dp[i][j] = bottom + right

        return dp[0][0]