class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [[0, 0] for _ in range(len(s) + 1)]
        for i in range(len(s) - 1, -1, -1):
            dp[i][0] = min(dp[i + 1][0] + (s[i] == '1'), dp[i + 1][1] + (s[i] == '0'))
            dp[i][1] = dp[i + 1][1] + (s[i] == '0')
        
        return dp[0][0]