class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        dp = [[[inf for _ in range(n + 2)] for _ in range(n + 2)] for _ in range(2 * n + 1)]

        for i in range(2 * n, -1, -1):
            for aCount in range(n, -1, -1):
                for bCount in range(n, -1, -1):
                    if i >= 2 * n:
                        dp[i][aCount][bCount] = 0
                    else:
                        dp[i][aCount][bCount] = min(
                            costs[i][0] + dp[i + 1][aCount + 1][bCount], 
                            costs[i][1] + dp[i + 1][aCount][bCount + 1]
                        )

        return dp[0][0][0]