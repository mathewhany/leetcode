class Node:
    def __init__(self, val, prev = None, next = None):
        self.val, self.prev, self.next = val, prev, next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = Node(homepage)
        

    def visit(self, url: str) -> None:
        node = Node(url, None, self.history)
        self.history.prev = node
        self.history = node
        

    def back(self, steps: int) -> str:
        for _ in range(steps):            
            if not self.history.next: break

            self.history = self.history.next

        return self.history.val

    def forward(self, steps: int) -> str:
        for _ in range(steps):
            if not self.history.prev:
                break

            self.history = self.history.prev
        
        return self.history.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)