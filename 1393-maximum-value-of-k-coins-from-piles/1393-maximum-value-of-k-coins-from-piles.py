class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        dp = [0 for _ in range(k + 1)]

        for i in range(len(piles) - 1, -1, -1):
            for needed in range(k, -1, -1):
                currentSum = 0
                for taken in range(min(needed, len(piles[i]))):
                    currentSum += piles[i][taken]
                    dp[needed] = max(dp[needed], currentSum + dp[needed - taken - 1])

        return dp[k]