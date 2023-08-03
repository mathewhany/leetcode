class SummaryRanges:

    def __init__(self):
        self.heap = []

    def addNum(self, value: int) -> None:
        heappush(self.heap, value)

    def getIntervals(self) -> List[List[int]]:
        numbers = []
        while self.heap: numbers.append(heappop(self.heap))

        ans = []

        prev = -inf
        last = -inf

        for n in numbers:
            if not ans or ans[-1][1] + 1 < n:
                ans.append([n, n])
            else:
                ans[-1][1] = n

            heappush(self.heap, n)

        return ans

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()