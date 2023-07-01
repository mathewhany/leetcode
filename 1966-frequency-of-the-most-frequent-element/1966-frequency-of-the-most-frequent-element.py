class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left = 0
        summ = 0
        best = 0

        for right, n in enumerate(nums):
            summ += n

            while (right - left + 1) * n - summ > k:
                summ -= nums[left]
                left += 1
            
            best = max(right - left + 1, best)
        
        return best