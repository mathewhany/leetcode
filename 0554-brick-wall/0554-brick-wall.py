class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        sizes = collections.defaultdict(int)
        mostFreq = 0

        for row in wall:
            currentSize = 0
            for brick in row[:-1]:
                currentSize += brick
                sizes[currentSize] += 1
                if sizes[currentSize] > mostFreq:
                    mostFreq = sizes[currentSize]
        
        return len(wall) - mostFreq