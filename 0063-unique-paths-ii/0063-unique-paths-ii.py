class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [0 for _ in range(n)]

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: 
                    dp[j] = 0
                elif (i, j) == (0, 0):
                    dp[j] = 1
                else:
                    top = dp[j] if i - 1 >= 0 else 0
                    left = dp[j - 1] if j - 1 >= 0 else 0
                    dp[j] = top + left

        return dp[n - 1]