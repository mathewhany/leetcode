class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        lo, hi = 1, num - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * mid >= num:
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans * ans == num