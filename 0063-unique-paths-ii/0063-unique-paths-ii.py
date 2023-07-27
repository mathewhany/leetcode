class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        
        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if not (0 <= i < m and 0 <= j < n) or obstacleGrid[i][j] == 1: return 0

            if (i, j) == (m - 1, n - 1): return 1

            memo[(i, j)] = ans = dp(i + 1, j) + dp(i, j + 1)

            return ans
        
        return dp(0, 0)