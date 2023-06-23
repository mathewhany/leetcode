class Solution:
    def sortColors(self, nums: List[int]) -> None:
        colors = [0, 0, 0]
        for n in nums: colors[n] += 1
        
        ans = []
        red, white, blue = colors
        
        for i in range(len(nums)):
            if red > 0:
                nums[i] = 0
                red -= 1
            elif white > 0:
                nums[i] = 1
                white -= 1
            elif blue > 0:
                nums[i] = 2
                blue -= 1
            