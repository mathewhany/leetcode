class Solution:
    def jump(self, nums: List[int]) -> int:
        minJumps = 0
        maxSoFar = 0
        nextMax = 0

        for i, n in enumerate(nums):
            if maxSoFar >= len(nums) - 1:
                break

            nextMax = max(nextMax, min(i + n, len(nums) - 1))
            if i == maxSoFar:
                maxSoFar = nextMax
                minJumps += 1
        
        return minJumps