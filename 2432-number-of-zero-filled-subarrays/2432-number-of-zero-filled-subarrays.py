class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        count = 0
        total = 0

        for i, n in enumerate(nums):
            if n == 0:
                count += 1
            
            if n != 0 or i == len(nums) - 1:
                total += count * (count + 1) // 2
                count = 0
        
        return total