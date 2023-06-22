class MyHashMap:
    size = 10000
    
    def _index(self, key):
        bucket = self.map[key % self.size]
        for i, (k, v) in enumerate(bucket):
            if k == key:
                return i, bucket
        return -1, bucket 


    def __init__(self):
        self.map = [[] for _ in range(self.size)]

    def put(self, key: int, value: int) -> None:
        i, bucket = self._index(key)
        if i == -1: bucket.append((key, value))
        bucket[i] = (key, value)

    def get(self, key: int) -> int:
        i, bucket = self._index(key)
        return bucket[i][1] if i != -1 else -1

    def remove(self, key: int) -> None:
        i, bucket = self._index(key)
        if i == -1: return
        bucket.pop(i)


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)