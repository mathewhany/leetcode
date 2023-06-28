class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        history = set()
        pre = 0
        for i, n in enumerate(nums): 
            cur = (pre + n) % k
            if i > 0 and (cur == 0 or n % k == 0 and nums[i - 1] % k == 0 or n % k != 0 and cur in history): 
                return True
            
            history.add(cur)
            pre = cur
        
        return False