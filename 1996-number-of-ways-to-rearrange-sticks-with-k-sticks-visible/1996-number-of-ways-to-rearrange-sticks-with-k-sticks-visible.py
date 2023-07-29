class Solution:
    def rearrangeSticks(self, n: int, k: int) -> int:
        mod = (10 ** 9 + 7)
        
        dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

        for remaining in range(n + 1):
            for required in range(k + 1):
                if remaining == required:
                    dp[remaining][required] = 1
                elif remaining == 0 or required == 0:
                    dp[remaining][required] = 0
                else:
                    dp[remaining][required] = (remaining - 1) * dp[remaining - 1][required] + dp[remaining - 1][required - 1]

        return dp[n][k] % mod
