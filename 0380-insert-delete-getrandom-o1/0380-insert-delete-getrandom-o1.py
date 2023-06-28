class RandomizedSet:

    def __init__(self):
        self.values = {}
        self.items = []

    def insert(self, val: int) -> bool:
        if val in self.values:
            return False
        
        self.values[val] = len(self.items)
        self.items.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val not in self.values: return False

        valIdx = self.values[val]
        self.values[self.items[-1]] = valIdx
        self.items[valIdx], self.items[-1] = self.items[-1], self.items[valIdx]
        self.items.pop()
        self.values.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.items)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()