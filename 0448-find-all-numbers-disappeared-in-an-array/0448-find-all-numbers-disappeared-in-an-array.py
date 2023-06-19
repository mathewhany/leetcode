class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        for i, n in enumerate(nums):
            nums[abs(n) - 1] = -1 * abs(nums[abs(n) - 1])
        
        res = []
        for i, n in enumerate(nums):
            if n > 0:
                res.append(i + 1)
        
        return res