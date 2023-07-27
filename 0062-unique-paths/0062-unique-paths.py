class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if (i, j) in memo: return memo[(i, j)]

            if not (0 <= i < m and 0 <= j < n): return 0

            if (i, j) == (m - 1, n - 1): return 1

            memo[(i, j)] = ans = dp(i + 1, j) + dp(i, j + 1)

            return ans
        
        return dp(0, 0)
            