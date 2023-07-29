class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        nCrimes = len(group)
        dp = [[0 for _ in range(minProfit + 1)] for _ in range(n + 1)]

        for i in range(nCrimes, -1, -1):
            for m in range(n, -1, -1):
                for totalProfit in range(minProfit + 1):
                    if i >= nCrimes: 
                        dp[m][totalProfit] = 1 if totalProfit >= minProfit else 0
                    else:
                        if m >= group[i]:
                            dp[m][totalProfit] += dp[m - group[i]][min(totalProfit + profit[i], minProfit)]
                        
                        dp[m][totalProfit] %= 10 ** 9 + 7


        return dp[n][0]