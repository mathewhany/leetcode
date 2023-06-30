class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        countZeros = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                countZeros += 1
            elif countZeros > 0:
                nums[i - countZeros] = nums[i]
                nums[i] = 0