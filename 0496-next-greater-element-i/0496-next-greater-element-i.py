class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = {}
        stack = []
        for i, n in enumerate(nums2):
            while stack and nums2[stack[-1]] < n:
                nextGreater[nums2[stack.pop()]] = n
            stack.append(i)

        ans = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            ans[i] = nextGreater[n] if n in nextGreater else -1
        
        return ans
        