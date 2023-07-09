# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, N: int) -> List[Optional[TreeNode]]:
        memo = {}

        def dfs(n):
            if n in memo:
                return memo[n]

            if n == 0: return []
            if n == 1: return [TreeNode(0)]

            ans = []

            for i in range(n - 1):
                left, right = i + 1, n - 1 - (i + 1)
                
                for l in dfs(left):
                    for r in dfs(right):
                        ans.append(TreeNode(0, l, r))
            
            memo[n] = ans

            return ans

        return dfs(N)