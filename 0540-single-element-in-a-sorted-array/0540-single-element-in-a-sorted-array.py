class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        lo, hi = 0, len(nums) - 1
        ans = -1

        while lo <= hi:
            mid = (lo + hi) // 2
            if mid % 2 == 0 and (mid == 0 or nums[mid - 1] != nums[mid]) or mid % 2 == 1 and nums[mid - 1] == nums[mid]:
                ans = mid
                lo = mid + 1
            else:
                hi = mid - 1
        
        return nums[ans]