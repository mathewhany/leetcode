class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        countDuplicates = 0
        last = 0

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                countDuplicates += 1
            else:
                nums[i - countDuplicates] = nums[i]
                last += 1
        return last