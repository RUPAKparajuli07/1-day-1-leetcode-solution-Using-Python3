from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if not obstacleGrid or not obstacleGrid[0]:
            return 0
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If the starting cell has an obstacle, there's no way to reach the end
        if obstacleGrid[0][0] == 1:
            return 0
        
        obstacleGrid[0][0] = 1
        
        # Filling the values for the first column
        for i in range(1, m):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)
        
        # Filling the values for the first row
        for j in range(1, n):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)
        
        # Filling the values for the rest of the grid
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0
        
        return obstacleGrid[-1][-1]
    
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        
        if not root.left and not root.right:
            return root.val == 1
        
        left_val = self.evaluateTree(root.left)
        right_val = self.evaluateTree(root.right)
        
        if root.val == 2:
            return left_val or right_val
        elif root.val == 3:
            return left_val and right_val
        else:
            return False
