class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones)
        target = stonesSum / 2
        memo = {}

        def dp(i, total):
            if (i, total) in memo: return memo[(i, total)]

            if total > target: return -inf
            if i >= len(stones): return total

            memo[(i, total)] = ans = max(
                dp(i + 1, total), 
                dp(i + 1, total + stones[i])
            )

            return ans
        
        S = dp(0, 0)

        return stonesSum - 2 * S