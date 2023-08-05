class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] = nums[i] << 10 | nums[n + i]
        
        end = 2 * n - 1
        for i in range(n - 1, -1, -1):
            x = nums[i] >> 10
            y = nums[i] & 0b1111111111

            nums[end] = y
            nums[end - 1] = x 
            end -= 2
        
        return nums