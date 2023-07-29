class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [[0 for _ in range(k + 1)] for _ in range(len(piles) + 1)]

        for i in range(len(piles) - 1, -1, -1):
            for needed in range(1, k + 1):
                ans = dp[i + 1][needed]
                currentSum = 0
                for taken in range(needed):
                    if taken >= len(piles[i]): break
                    currentSum += piles[i][taken]
                    ans = max(ans, currentSum + dp[i + 1][needed - taken - 1])
                dp[i][needed] = ans

        return dp[0][k]