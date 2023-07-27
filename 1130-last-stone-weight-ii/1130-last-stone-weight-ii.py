class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stonesSum = sum(stones)
        target = stonesSum // 2
        dp = [[0 for _ in range(target + 1)] for _ in range(len(stones))]

        for i in range(len(stones) - 1, -1, -1):
            for total in range(target, -1, -1):
                if i + 1 >= len(stones):
                    dp[i][total] = max(
                        total,
                        total + stones[i] if total + stones[i] <= target else -inf
                    )
                else:
                    dp[i][total] = max(
                        dp[i + 1][total],
                        dp[i + 1][total + stones[i]] if total + stones[i] <= target else -inf
                    )


        S = dp[0][0]

        return stonesSum - 2 * S