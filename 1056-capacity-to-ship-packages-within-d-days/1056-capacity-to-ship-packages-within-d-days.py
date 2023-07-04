class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def valid(capacity):
            count = 1
            currentSum = 0
            for w in weights:
                if w > capacity:
                    return False
                if currentSum + w > capacity:
                    count += 1
                    currentSum = w
                else:
                    currentSum += w
            return count <= days
        
        lo, hi = 1, sum(weights)
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if valid(mid):
                ans = mid
                hi = mid - 1
            else:
                lo = mid + 1
        
        return ans