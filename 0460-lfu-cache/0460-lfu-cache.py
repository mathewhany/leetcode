class ListNode:
    def __init__(self, key = 0, next = None, prev = None):
        self.key, self.next, self.prev = key, next, prev

class DoublyLinkedList:

    def __init__(self):
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.key_to_node = {}
        self.size = 0
    

    def pushRight(self, key):
        node = ListNode(key, self.tail, self.tail.prev)
        node.prev.next = node
        node.next.prev = node
        self.size += 1
        self.key_to_node[key] = node
    

    def pushLeft(self, key):
        node = ListNode(key, self.head.next, self.head)
        node.prev.next = node
        node.next.prev = node
        self.size += 1
        self.key_to_node[key] = node


    def popRight(self):
        if self.size > 0:
            lastNode = self.tail.prev
            lastNode.prev.next = lastNode.next
            lastNode.next.prev = lastNode.prev
            self.key_to_node.pop(lastNode.key)
            self.size -= 1
            lastNode.prev, lastNode.next = None, None
            return lastNode.key
        return -1
    

    def popLeft(self):
        if self.size > 0:
            firstNode = self.head.next
            firstNode.prev.next = firstNode.next
            firstNode.next.prev = firstNode.prev
            self.key_to_node.pop(firstNode.key)
            self.size -= 1
            firstNode.prev, firstNode.next = None, None
            return firstNode.key
        return -1

    
    def pop(self, key):
        if key in self.key_to_node:
            node = self.key_to_node[key]
            node.prev.next = node.next
            node.next.prev = node.prev
            node.next, node.prev = None, None
            self.key_to_node.pop(key)
            self.size -= 1
            return node.key
        return -1

    
    def __len__(self):
        return self.size


    def __str__(self):
        ans = []
        cur = self.head.next
        while cur != self.tail:
            ans.append(str(cur.key))
            cur = cur.next
        return ' '.join(ans)

class LFUCache:

    def __init__(self, capacity: int):
        self.key_to_val = {}
        self.lfu_count = 1
        self.key_to_count = defaultdict(int)
        self.count_to_list = defaultdict(DoublyLinkedList)
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key in self.key_to_val:
            self._update_count(key)
            return self.key_to_val[key]
        return -1


    def put(self, key: int, value: int) -> None:
        if len(self.key_to_val) >= self.capacity and key not in self.key_to_val:
            removedKey = self.count_to_list[self.lfu_count].popLeft()
            self.key_to_count.pop(removedKey)
            self.key_to_val.pop(removedKey)

        self.key_to_val[key] = value
        self._update_count(key)
        self.lfu_count = min(self.lfu_count, self.key_to_count[key])
        
            
    def _update_count(self, key):
        oldCount = self.key_to_count[key]
        self.key_to_count[key] += 1
        self.count_to_list[oldCount].pop(key)
        self.count_to_list[oldCount + 1].pushRight(key)

        if self.lfu_count == oldCount and len(self.count_to_list[oldCount]) == 0:
            self.lfu_count += 1
# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)