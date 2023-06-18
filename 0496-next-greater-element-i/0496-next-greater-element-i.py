class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nextGreater = [-1] * len(nums2)
        positions = {}
        stack = []
        for i, n in enumerate(nums2):
            positions[n] = i
            while stack and nums2[stack[-1]] < n:
                nextGreater[stack.pop()] = n
            stack.append(i)

        ans = [-1] * len(nums1)
        for i, n in enumerate(nums1):
            ans[i] = nextGreater[positions[n]] if n in positions else -1
        
        return ans
        