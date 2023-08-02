class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        currentMax = nums[0]
        excess = 0
        sumSoFar = nums[0]

        for i in range(1, len(nums)):
            sumSoFar += nums[i]
            
            if nums[i] - currentMax > excess:
                nums[i] -= excess
                currentMax += ceil((nums[i] - currentMax) / (i + 1))

            excess = currentMax * (i + 1) - sumSoFar

        return currentMax
                