from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        perimeter = 0

        for i in range(rows):
            for j in range(cols):
                # Check only land cells
                if grid[i][j] == 1:
                    # Each land cell contributes 4 to the perimeter
                    perimeter += 4
                    
                    # Subtract 2 for each shared edge with another land cell (up and left)
                    if i > 0 and grid[i-1][j] == 1:  # check top
                        perimeter -= 2
                    if j > 0 and grid[i][j-1] == 1:  # check left
                        perimeter -= 2

        return perimeter
