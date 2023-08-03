from sortedcontainers import SortedDict

class SummaryRanges:

    def __init__(self):
        self.map = SortedDict()

    def addNum(self, value: int) -> None:
        if value in self.map: return

        right = self.map.bisect_left(value)
        left = right - 1

        keyRight = self.map.peekitem(right)[0] if right < len(self.map) else -1
        keyLeft = self.map.peekitem(left)[0] if left >= 0 else -1
        
        if (keyRight != -1 and keyLeft != -1 and self.map[keyLeft] + 1 == value and value + 1 == keyRight):
            self.map[keyLeft] = self.map[keyRight]
            self.map.pop(keyRight)
        elif (right != -1 and keyRight == value + 1):
            self.map[value] = self.map.pop(keyRight)
        elif (left != -1 and self.map[keyLeft] + 1 >= value):
            self.map[keyLeft] = max(self.map[keyLeft], value)
        else:
            self.map[value] = value

    def getIntervals(self) -> List[List[int]]:
        ans = []        
        for start in self.map:
            ans.append([start, self.map[start]])
        return ans
        

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()