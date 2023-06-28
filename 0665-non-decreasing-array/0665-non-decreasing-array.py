class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        pre = -inf
        mistake = -1

        for i, n in enumerate(nums):
            if n < pre:
                if mistake >= 0:
                    return False
                mistake = i
                pre = -inf
            else:
                pre = n
        
        if mistake < 0 or mistake == len(nums) - 1: return True

        n0 = nums[mistake - 2] if mistake >= 2 else -inf
        n1 = nums[mistake - 1]
        n2 = nums[mistake]
        n3 = nums[mistake + 1]

        if n0 > n3: return False

        if not (n0 <= n2 <= n3 or n0 <= n1 <= n3): return False

        return True