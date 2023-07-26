class Solution:
    def longestObstacleCourseAtEachPosition(self, nums: List[int]) -> List[int]:
        dp = []
        ans = []

        for n in nums:
            if not dp or dp[-1] <= n:
                dp.append(n)
                ans.append(len(dp))
            else:
                idx = bisect_right(dp, n)
                ans.append(idx + 1)
                
                dp[idx] = n
        
        return ans

