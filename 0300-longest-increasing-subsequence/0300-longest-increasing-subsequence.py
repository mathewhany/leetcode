class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1 for _ in range(len(nums))]
        best = 1

        for i, n in enumerate(nums):
            for j, prev in enumerate(nums[:i]):
                if n > prev:
                    dp[i] = max(dp[i], dp[j] + 1)
                    best = max(dp[i], best)

        return best