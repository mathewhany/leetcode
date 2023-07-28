class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if not (0 <= i < m and 0 <= j < n):
                return inf
            
            if (i, j) == (m - 1, n - 1): return grid[i][j]

            memo[(i, j)] = ans = grid[i][j] + min(dp(i + 1, j), dp(i, j + 1))

            return ans
        
        return dp(0, 0)
