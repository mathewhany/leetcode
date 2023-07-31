class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if i in memo: return memo[i]

            if i >= len(nums) - 1:
                return 0

            ans = inf
            
            for j in range(i + 1, i + nums[i] + 1):
                ans = min(
                    1 + dp(j),
                    ans
                )

            memo[i] = ans
            
            return ans
        
        return dp(0)
        