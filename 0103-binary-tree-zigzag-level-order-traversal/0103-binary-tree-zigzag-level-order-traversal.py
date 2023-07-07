# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque([root] if root else [])
        ltr = True
        ans = []

        while queue:
            ans.append([])
            for _ in range(len(queue)):
                if ltr:
                    current = queue.popleft()
                    if current.left:
                        queue.append(current.left)
                    if current.right:
                        queue.append(current.right)
                    
                else:
                    current = queue.pop()
                    if current.right:
                        queue.appendleft(current.right)
                    if current.left:
                        queue.appendleft(current.left)
                ans[-1].append(current.val)

            ltr = not ltr
        
        return ans
            


