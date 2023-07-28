class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        memo = {}

        def dp(i, shouldAdd):
            if (i, shouldAdd) in memo: return memo[(i, shouldAdd)]

            if i >= len(nums): return 0

            memo[(i, shouldAdd)] = ans = max(
                (nums[i] if shouldAdd else -nums[i]) + dp(i + 1, not shouldAdd),
                dp(i + 1, shouldAdd)
            )

            return ans
        
        return dp(0, True)