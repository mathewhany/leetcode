class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            n = nums[i]
            if n > 0 and n - 1 < len(nums) and n != i + 1 and nums[n - 1] != nums[i]:
                nums[n - 1], nums[i] = nums[i], nums[n - 1]
            else:
                i += 1

        for i, n in enumerate(nums):
            if n != i + 1:
                return i + 1
        
        return len(nums) + 1