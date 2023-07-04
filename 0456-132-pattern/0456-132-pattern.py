class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        for n in nums:
            one = n
            while stack and stack[-1][1] <= n:
                one = min(one, stack.pop()[0])
            if stack and stack[-1][0] < n < stack[-1][1]:
                return True
            stack.append((one, n))
        return False