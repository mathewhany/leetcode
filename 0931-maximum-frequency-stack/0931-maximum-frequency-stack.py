class FreqStack:

    def __init__(self):
        self.freq = defaultdict(int)
        self.heap = []
        self.t = 0
        

    def push(self, val: int) -> None:
        self.freq[val] += 1
        heappush(self.heap, (-self.freq[val], -self.t, val))
        self.t += 1

    def pop(self) -> int:
        _, _, val = heappop(self.heap)
        self.freq[val] -= 1
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()