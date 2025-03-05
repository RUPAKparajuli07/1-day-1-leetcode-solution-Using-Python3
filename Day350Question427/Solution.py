from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        def isUniform(x1, y1, x2, y2):
            """Check if all elements in the subgrid are the same."""
            val = grid[x1][y1]
            for i in range(x1, x2):
                for j in range(y1, y2):
                    if grid[i][j] != val:
                        return False, None
            return True, val
        
        def build(x1, y1, x2, y2):
            """Recursively construct the Quad-Tree."""
            uniform, val = isUniform(x1, y1, x2, y2)
            if uniform:
                return Node(val == 1, True)
            
            midX, midY = (x1 + x2) // 2, (y1 + y2) // 2
            
            return Node(
                val=True,  # Can be True/False, doesn't matter for non-leaf nodes
                isLeaf=False,
                topLeft=build(x1, y1, midX, midY),
                topRight=build(x1, midY, midX, y2),
                bottomLeft=build(midX, y1, x2, midY),
                bottomRight=build(midX, midY, x2, y2)
            )
        
        return build(0, 0, len(grid), len(grid))
