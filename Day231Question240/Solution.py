from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Start from the top-right corner
        row, col = 0, len(matrix[0]) - 1
        
        # While within the boundaries of the matrix
        while row < len(matrix) and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1  # Move left
            else:
                row += 1  # Move down
                
        # If we exit the loop, the target was not found
        return False
