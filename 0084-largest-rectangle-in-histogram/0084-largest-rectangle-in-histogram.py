class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        best = 0

        for i, h in enumerate(heights):
            start = i
            while stack:
                prevStart, prevHeight = stack[-1]
                if prevHeight <= h:
                    break
                start = prevStart
                stack.pop()
                best = max((i - prevStart) * prevHeight, best)
            stack.append((start, h))

        while stack:
            prevStart, prevHeight = stack.pop()
            best = max((len(heights) - prevStart) * prevHeight, best)
        
        return best