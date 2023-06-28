class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i, n in enumerate(nums):
            if n < 0:
                nums[i] = 0
        for i, n in enumerate(nums):
            val = abs(n)
            if 0 <= val - 1 <= len(nums) - 1:
                cur = nums[val - 1]
                if cur == 0:
                    nums[val - 1] = -1 * val
                else:
                    nums[val - 1] = -1 * abs(cur)
        
        for i, n in enumerate(nums):
            if n >= 0:
                return i + 1
        
        return len(nums) + 1