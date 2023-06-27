class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        groups = collections.defaultdict(int)

        for width, height in rectangles:
            groups[width / height] += 1
        
        ans = 0
        for group in groups:
            n = groups[group]
            if n > 1:
                ans += n * (n - 1) // 2
        
        return ans