class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        
        if totalSum % 2 == 1:
            return False

        dp = [True] + [False] * (totalSum // 2)

        for n in nums:
            for i in range(totalSum // 2, 0, -1):
                dp[i] = dp[i] or i - n >= 0 and dp[i - n]

        return dp[totalSum // 2]