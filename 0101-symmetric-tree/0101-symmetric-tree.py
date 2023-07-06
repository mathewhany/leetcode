# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        stackLeft, stackRight = [root.left], [root.right]

        while stackLeft and stackRight:
            left, right = stackLeft.pop(), stackRight.pop()

            if left and right and left.val == right.val:
                stackLeft.append(left.left)
                stackLeft.append(left.right)

                stackRight.append(right.right)
                stackRight.append(right.left)
            elif not left and not right:
                continue
            else:
                return False
        
        return not stackLeft and not stackRight

