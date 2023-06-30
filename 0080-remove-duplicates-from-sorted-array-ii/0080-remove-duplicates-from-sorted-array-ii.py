class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0
        for i in range(len(nums)):
            if not (i + 2 < len(nums) and nums[i] == nums[i + 2]):
                nums[left] = nums[i]
                left += 1
        return left