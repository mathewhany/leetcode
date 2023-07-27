class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + (dp[i - 1][j - 1] if i - 1 >= 0 and j - 1 >= 0 else 0)
                else:
                    dp[i][j] = max(
                        dp[i - 1][j] if i - 1 >= 0 else 0,
                        dp[i][j - 1] if j - 1 >= 0 else 0
                    )

        return dp[n - 1][m - 1]