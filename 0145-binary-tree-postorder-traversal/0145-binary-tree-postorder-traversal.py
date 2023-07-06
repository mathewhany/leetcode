# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        ans = []
        stack = [root]

        while stack:
            cur = stack.pop()

            if cur:
                ans.append(cur.val)
                stack.append(cur.left)
                stack.append(cur.right)


        return reversed(ans)