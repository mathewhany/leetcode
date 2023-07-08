"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def constructTree(startX, endX, startY, endY):
            if startX > endX or startY > endY: return

            if startX == endX and startY == endY: return Node(grid[startY][startX], True)

            midX, midY = (startX + endX) // 2, (startY + endY) // 2
            
            topLeft = constructTree(startX, midX, startY, midY)
            topRight = constructTree(midX + 1, endX, startY, midY)
            bottomLeft = constructTree(startX, midX, midY + 1, endY)
            bottomRight = constructTree(midX + 1, endX, midY + 1, endY)

            children = [topLeft, topRight, bottomLeft, bottomRight]

            if all([node.isLeaf and node.val == 0 for node in children]):
                return Node(0, True)
            elif all([node.isLeaf and node.val == 1 for node in children]):
                return Node(1, True)
            else:
                return Node(1, False, topLeft, topRight, bottomLeft, bottomRight)
        
        n = len(grid)

        return constructTree(0, n - 1, 0, n - 1)
