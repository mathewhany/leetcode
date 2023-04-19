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
                return 0, 0

            leftSplit, leftNoSplit = dfs(current.left)
            rightSplit, rightNoSplit = dfs(current.right)

            split = current.val + max(leftNoSplit, 0) + max(rightNoSplit, 0)
            noSplit = current.val + max(leftNoSplit, rightNoSplit)

            best = max(best, split, noSplit)

            return max(split, 0), max(noSplit, 0)

        dfs(root)

        return best