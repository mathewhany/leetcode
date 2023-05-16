class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        letterLastOccurence = {}
        for i, l in enumerate(s):
            letterLastOccurence[l] = i
        
        counts = []
        start, end = 0, 0
        for i, l in enumerate(s):
            if i > end:
                counts.append(end - start + 1)
                start, end = i, i
            end = max(end, letterLastOccurence[l])
        counts.append(end - start + 1)
        return counts
