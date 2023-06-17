class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxCount = 0
        maxNum = 0
        for num, count in Counter(nums).items():
            if count >= maxCount:
                maxCount = count
                maxNum = num
        
        return maxNum
