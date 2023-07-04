class Solution:
    def arrangeCoins(self, n: int) -> int:
        lo, hi = 1, n
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid * (mid + 1) // 2 <= n:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return ans