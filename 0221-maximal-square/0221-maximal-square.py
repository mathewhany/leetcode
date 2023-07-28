class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n)] for _ in range(m)]
        best = 0

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    top = dp[i - 1][j] if i - 1 >= 0 else 0
                    left = dp[i][j - 1] if j - 1 >= 0 else 0
                    topleft = dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0

                    sideLen = min(
                        sqrt(top),
                        sqrt(left),
                        sqrt(topleft)
                    ) + 1

                    dp[i][j] = int(sideLen ** 2)
                
                best = max(best, dp[i][j])

        return best