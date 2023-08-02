class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        memo = {}

        def dp(i, aCount, bCount):
            if (i, aCount, bCount) in memo: return memo[(i, aCount, bCount)]
            if aCount > n or bCount > n: return inf

            if i >= 2 * n: 
                return 0

            cost1 = costs[i][0] + dp(i + 1, aCount + 1, bCount)
            cost2 = costs[i][1] + dp(i + 1, aCount, bCount + 1)

            memo[(i, aCount, bCount)] = ans = min(cost1, cost2)

            return ans
        
        return dp(0, 0, 0)