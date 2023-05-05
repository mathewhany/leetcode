class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        best = nums[0]
        minSoFar, maxSoFar = nums[0], nums[0]

        for i in range(1, len(nums)):
            n = nums[i]
            candidates = [
                n * minSoFar, 
                n * maxSoFar,
                n
            ]
            minSoFar = min(candidates)
            maxSoFar = max(candidates)
            best = max(best, maxSoFar)

        return best


