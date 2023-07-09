class LockingTree:

    def __init__(self, parent: List[int]):
        self.locks = {}
        self.children = defaultdict(list)
        self.parent = parent

        for i, p in enumerate(parent):
            self.children[p].append(i)

    def lock(self, num: int, user: int) -> bool:
        if num not in self.locks:
            self.locks[num] = user
            return True
        return False

    def unlock(self, num: int, user: int) -> bool:
        if num in self.locks and self.locks[num] == user:
            self.locks.pop(num)
            return True
        return False

    def upgrade(self, num: int, user: int) -> bool:
        curr = num
        while curr != -1 and curr not in self.locks:
            curr = self.parent[curr]
        if curr != -1: 
            return False

        def dfs(node):
            ans = False

            for child in self.children[node]:
                if child in self.locks: 
                    ans = True
                    self.locks.pop(child)

                if dfs(child): 
                    ans = True

            return ans

        if not dfs(num): return False
        
        self.lock(num, user)
        
        return True

            


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)