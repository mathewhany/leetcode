# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.current = root

    def next(self) -> int:
        while self.current:
            self.stack.append(self.current)
            self.current = self.current.left

        parent = self.stack.pop()
        self.current = parent.right
        return parent.val

    def hasNext(self) -> bool:
        return self.current is not None or len(self.stack) > 0         


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()