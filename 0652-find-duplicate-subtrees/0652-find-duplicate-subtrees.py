# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        trees = defaultdict(list)
        ans = []
        def dfs(node):
            if not node:
                return '-'
            
            tree = ' '.join([str(node.val), dfs(node.left), dfs(node.right)])
            trees[tree].append(node)

            if len(trees[tree]) == 2:
                ans.append(node)
            
            return tree

        
        dfs(root)

        return ans

