from heapq import *

class MedianFinder:
    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num: int) -> None:
        heapq.heappush(self.minHeap, -heapq.heappushpop(self.maxHeap, -num))
        if abs(len(self.minHeap) - len(self.maxHeap)) > 1:
            heapq.heappush(self.maxHeap, -heapq.heappop(self.minHeap))
            
    def findMedian(self) -> float:
        if (len(self.maxHeap) + len(self.minHeap)) % 2 == 0:
            return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        return self.minHeap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()