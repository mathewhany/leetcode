class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        dp = [[inf for _ in range(len(cuts))] for _ in range(len(cuts))]
        
        for i in range(len(cuts) - 1, -1, -1):
            start = cuts[i]
            for j in range(i + 1, len(cuts)):
                end = cuts[j]
                for cut in range(i + 1, j):
                    dp[i][j] = min(
                        dp[i][j],
                        (end - start) + dp[i][cut] + dp[cut][j]
                    )
                dp[i][j] = dp[i][j] if dp[i][j] != inf else 0

        return dp[0][len(cuts) - 1]