class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        best = nums[0]
        for i in range(1, N):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
            best = max(best, nums[i])
        return best
            