class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(k + 1)]

        for i in range(len(piles) - 1, -1, -1):
            for needed in range(k, -1, -1):
                ans = dp[needed]
                currentSum = 0
                for taken in range(needed):
                    if taken >= len(piles[i]): break
                    currentSum += piles[i][taken]
                    ans = max(ans, currentSum + dp[needed - taken - 1])
                dp[needed] = ans

        return dp[k]