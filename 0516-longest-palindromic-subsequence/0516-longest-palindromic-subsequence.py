class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0 for _ in range(n)] for _ in range(n)]

        for end in range(n):
            for start in range(end, -1, -1):
                if start == end:
                    dp[start][end] = 1
                else:
                    dp[start][end] = max(
                        (2 if s[start] == s[end] else 0) + (dp[start + 1][end - 1] if start + 1 <= end - 1 else 0),
                        dp[start + 1][end] if start + 1 <= end else 0,
                        dp[start][end - 1] if end - 1 >= start else 0
                    )

        return dp[0][n - 1]
