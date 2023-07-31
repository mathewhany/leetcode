class Solution:
    def jump(self, nums: List[int]) -> int:
        start, end = 0, 1
        nextStart, nextEnd = 1, 1
        jumps = 0

        for i in range(len(nums)):
            if i >= end:
                start, end = nextStart, nextEnd
                nextStart, nextEnd = end + 1,  end + 1
                jumps += 1
            
            if i < end:
                nextEnd = max(nextEnd, i + nums[i] + 1)
            else:
                break
        
        if nextEnd > len(nums) - 1:
            return jumps
        
        return -1
            
