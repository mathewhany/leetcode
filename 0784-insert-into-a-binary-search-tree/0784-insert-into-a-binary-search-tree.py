# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def insert(node):
            if not node:
                return TreeNode(val)
            
            if val > node.val:
                node.right = insert(node.right)
            else:
                node.left = insert(node.left)
            
            return node
        
        return insert(root)