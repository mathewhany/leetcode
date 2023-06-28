class Solution:
    def arraySign(self, nums: List[int]) -> int:
        sign = 1
        for n in nums:
            if n == 0: return 0

            sign *= -1 if n < 0 else 1
        return sign