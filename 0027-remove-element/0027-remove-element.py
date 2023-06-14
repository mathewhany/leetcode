class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = len(nums)
        i = 0
        while i < len(nums):
            if nums[i] == val:
                count -= 1
                del nums[i]
            else:
                i += 1
        return count