class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        currentMax = -inf
        maxFromStart = [-inf for _ in range(len(nums))]
        maxFromEnd = [-inf for _ in range(len(nums))]
        last = 0
        currentSum = 0
        best = -inf
        for i, n in enumerate(nums):
            currentSum += n
            maxFromStart[i] = max(maxFromStart[i - 1], currentSum) if i - 1 >= 0 else currentSum
            currentMax = max(n, currentMax + n)
            best = max(currentMax, best)

        currentSum = 0
        maxFromEnd = -inf

        for i in range(len(nums) - 1, 0, -1):
            currentSum += nums[i]
            maxFromEnd = max(maxFromEnd, currentSum)
            
            best = max(
                maxFromStart[i - 1] + maxFromEnd,
                best
            )


        return best