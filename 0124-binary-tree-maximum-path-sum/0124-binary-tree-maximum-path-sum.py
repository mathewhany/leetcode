# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = -inf

        def dfs(current):
            nonlocal best

            if not current:
                return 0

            leftMax = max(dfs(current.left), 0)
            rightMax = max(dfs(current.right), 0)

            best = max(best, current.val + leftMax + rightMax)

            return current.val + max(leftMax, rightMax)

        dfs(root)

        return best