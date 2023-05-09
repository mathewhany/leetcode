class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(i, current):
            if (i, current) in memo:
                return memo[(i, current)]

            if i >= len(nums):
                return 1 if current == target else 0
            
            answer = memo[(i, current)] = dp(i + 1, current + nums[i]) + dp(i + 1, current - nums[i])

            return answer

        return dp(0, 0)