class Solution:
    def maxScore(self, nums: List[int]) -> int:
        memo = {}

        def dp(i):
            if (i, tuple(nums)) in memo: return memo[(i, tuple(nums))]

            if i > len(nums) // 2: 
                return 0

            best = -inf

            for j in range(len(nums)):
                if nums[j] == -1: continue
                for k in range(j + 1, len(nums)):
                    if nums[k] == -1: continue
                    x, y = nums[j], nums[k]
                    nums[j], nums[k] = -1, -1
                    best = max(best, i * gcd(x, y) + dp(i + 1))
                    nums[j], nums[k] = x, y
            
            memo[(i, tuple(nums))] = best

            return best
        
        return dp(1)