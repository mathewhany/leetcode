class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()

        best = inf
        for i in range(0, len(nums) - k + 1):
            for j in range(i + k - 1, len(nums)):
                best = min(best, nums[j] - nums[i])
        
        return best