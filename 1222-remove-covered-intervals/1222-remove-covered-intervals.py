class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        lastStart, lastEnd = -1, -1
        removed = 0
        
        for start, end in sorted(intervals, key=lambda x: (x[0], -x[1])):
            if start <= lastEnd:
                if end <= lastEnd:
                    removed += 1
                lastEnd = max(end, lastEnd)
            else:
                lastStart, lastEnd = start, end
                
        return len(intervals) - removed

