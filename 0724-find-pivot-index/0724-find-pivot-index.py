class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total = sum(nums)
        currentSum = 0
        for i in range(len(nums)):
            if currentSum == total - currentSum - nums[i]:
                return i
            
            currentSum += nums[i]
        return -1