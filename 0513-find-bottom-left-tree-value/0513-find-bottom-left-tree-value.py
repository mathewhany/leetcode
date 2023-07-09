# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        if not root: return

        leftMost = None
        queue = deque([root])

        while queue:
            leftMost = queue[0]
            for _ in range(len(queue)):
                current = queue.popleft()
                if current.left: queue.append(current.left)
                if current.right: queue.append(current.right)
        
        return leftMost.val