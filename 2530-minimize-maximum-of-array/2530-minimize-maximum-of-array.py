class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        lo, hi = 0, 10 ** 9
        ans = -1

        def ok(maxVal):
            excess = 0
            for n in nums:
                if n <= maxVal:
                    excess += maxVal - n
                else:
                    if n - maxVal > excess:
                        return False
                    
                    excess -= n - maxVal
            return True

        while lo <= hi:
            mid = (lo + hi) // 2
            if ok(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans
