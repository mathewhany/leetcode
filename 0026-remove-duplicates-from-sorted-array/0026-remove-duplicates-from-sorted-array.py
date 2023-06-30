class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        left = 0

        for i in range(len(nums)):
            if not (i + 1 < len(nums) and nums[i] == nums[i + 1]):
                nums[left] = nums[i]
                left += 1

        return left