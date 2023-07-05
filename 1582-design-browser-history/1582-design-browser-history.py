class BrowserHistory:

    def __init__(self, homepage: str):
        self.stack = [homepage]
        self.forwardStack = []
        

    def visit(self, url: str) -> None:
        self.stack.append(url)
        self.forwardStack = []
        

    def back(self, steps: int) -> str:
        for _ in range(min(steps, len(self.stack) - 1)):
            self.forwardStack.append(self.stack.pop())
        
        return self.stack[-1]

    def forward(self, steps: int) -> str:
        for _ in range(min(steps, len(self.forwardStack))):
            self.stack.append(self.forwardStack.pop())
        
        return self.stack[-1]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)