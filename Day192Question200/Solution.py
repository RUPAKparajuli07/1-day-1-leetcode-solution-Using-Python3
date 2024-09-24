from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # If the grid is empty, return 0
        if not grid:
            return 0
        
        # Dimensions of the grid
        m, n = len(grid), len(grid[0])
        
        # Function to perform DFS to mark the connected '1's as visited
        def dfs(i, j):
            # Boundary check and if the cell is already water ('0'), return
            if i < 0 or i >= m or j < 0 or j >= n or grid[i][j] == '0':
                return
            # Mark the current cell as visited by changing '1' to '0'
            grid[i][j] = '0'
            # Visit all four directions (up, down, left, right)
            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)
        
        # Counter for number of islands
        count = 0
        
        # Traverse each cell in the grid
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':  # If we encounter a '1'
                    count += 1        # We found a new island
                    dfs(i, j)         # Perform DFS to mark the entire island
        
        # Return the total number of islands
        return count
