class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        memo = {}

        def dp(i, needed):
            if (i, needed) in memo: return memo[(i, needed)]

            if needed == 0 or i >= len(piles): return 0

            ans = dp(i + 1, needed)
            currentSum = 0

            for taken in range(needed):
                if taken >= len(piles[i]): break

                currentSum += piles[i][taken]
                ans = max(ans, currentSum + dp(i + 1, needed - (taken + 1)))

            memo[(i, needed)] = ans
            
            return ans
        
        return dp(0, k)