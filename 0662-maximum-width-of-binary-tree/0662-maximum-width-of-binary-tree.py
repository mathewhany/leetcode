# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: return 0

        queue = deque([(root, 0)])
        best = 1

        while queue:
            if len(queue) >= 2:
                start = queue[0][1]
                end = queue[-1][1]
                best = max(best, end - start + 1)

            for _ in range(len(queue)):
                current, i = queue.popleft()
                if current.left:
                    queue.append((current.left, 2 * i))
                if current.right:
                    queue.append((current.right, 2 * i + 1))
        
        return best