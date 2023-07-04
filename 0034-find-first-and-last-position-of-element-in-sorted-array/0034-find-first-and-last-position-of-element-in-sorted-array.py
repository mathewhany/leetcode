class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        lo, hi = 0, len(nums) - 1
        start = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] >= target:
                start = mid
                hi = mid - 1
            else:
                lo = mid + 1

        lo, hi = 0, len(nums) - 1
        end = -1
        while lo <= hi:
            mid = (lo + hi) // 2
            if nums[mid] <= target:
                end = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        if start == -1 or nums[start] != target:
            return [-1, -1]
        
        return [start, end]
        