class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        ADD, SUB = 0, 1
        dp = [0 for _ in range(2)]

        for i in range(len(nums) - 1, -1, -1):
            for j in [ADD, SUB]:
                dp[j] = max(
                    (nums[i] if j == ADD else -nums[i]) + dp[(j + 1) % 2],
                    dp[j]
                )

        return dp[0]