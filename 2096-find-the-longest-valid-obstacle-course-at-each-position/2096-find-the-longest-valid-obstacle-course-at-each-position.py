
class SegmentTree:
    def __init__(self, size):
        self.size = int(2 ** ceil(log2(size)))
        self.tree = [0] * (2 * self.size)

    def findMax(self, start, end):
        def findMax(targetStart, targetEnd, currentStart, currentEnd, currentIndex):
            if targetEnd < currentStart or targetStart > currentEnd:
                return -inf

            if targetStart <= currentStart and targetEnd >= currentEnd:
                return self.tree[currentIndex]

            mid = (currentStart + currentEnd) // 2

            return max(
                findMax(targetStart, targetEnd, currentStart, mid, 2 * currentIndex),
                findMax(targetStart, targetEnd, mid + 1, currentEnd, 2 * currentIndex + 1)
            )
        
        return findMax(start, end, 0, self.size - 1, 1)
    
    def get(self, index):
        return self.tree[self.size + index]

    def update(self, index, value):
        self.tree[self.size + index] = value

        parent = (self.size + index) // 2
        while parent > 0:
            self.tree[parent] = max(self.tree[2 * parent], self.tree[2 * parent + 1])
            parent //= 2

def compactArray(arr):
    sortedArr = sorted(list(set(arr)))

    return [bisect_left(sortedArr, n) for n in arr]

class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        lis = []
        for i, x in enumerate(obstacles):
            if len(lis) == 0 or lis[-1] <= x:  # Append to LIS if new element is >= last element in LIS
                lis.append(x)
                obstacles[i] = len(lis)
            else:
                idx = bisect_right(lis, x)  # Find the index of the smallest number > x
                lis[idx] = x  # Replace that number with x
                obstacles[i] = idx + 1
        return obstacles
