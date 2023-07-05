class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        lo, hi = max(nums), sum(nums)
        ans = -1

        def valid(mid):
            groups = 1
            curSum = 0
            for n in nums:
                if curSum + n > mid:
                    curSum = n
                    groups += 1
                else:
                    curSum += n
            return groups <= k
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans