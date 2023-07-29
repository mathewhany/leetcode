class Solution:
    def profitableSchemes(self, n: int, minProfit: int, group: List[int], profit: List[int]) -> int:
        nCrimes = len(group)
        maxProfit = sum(profit)
        dp = defaultdict(int)

        for i in range(nCrimes, -1, -1):
            for available in range(n + 1):
                for totalProfit in range(minProfit + 1, -1, -1):
                    if i >= nCrimes: 
                        dp[(i, available, totalProfit)] = 1 if totalProfit >= minProfit else 0
                    else:
                        dp[(i, available, totalProfit)] = dp[i + 1, available, totalProfit]

                        if available >= group[i]:
                            dp[(i, available, totalProfit)] += dp[(i + 1, available - group[i], min(minProfit, totalProfit + profit[i]))]
                        
                        dp[(i, available, totalProfit)] %= 10 ** 9 + 7


        return dp[(0, n, 0)]