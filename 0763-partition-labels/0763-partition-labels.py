class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndex = {}
        for i, l in enumerate(s):
            lastIndex[l] = i
        
        counts = []
        start, end = 0, 0
        for i, l in enumerate(s):
            end = max(end, lastIndex[l])
            if i == end:
                counts.append(end - start + 1)
                start, end = i + 1, i + 1

        return counts
