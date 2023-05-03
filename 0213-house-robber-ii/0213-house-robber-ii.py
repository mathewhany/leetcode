class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(start, end):
            if start >= len(nums):
                return 0
             
            prev1, prev2 = 0, 0
            best = nums[start]

            for i in range(start, end):
                prev1, prev2 = max(prev1, prev2 + nums[i]), prev1      
                best = max(best, prev1)

            return best
        
        return max(dp(0, len(nums) - 1), dp(1, len(nums)))