from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        
        # Iterate through each layer
        for layer in range(n // 2):
            first = layer
            last = n - 1 - layer
            
            # Iterate through each element in the layer
            for i in range(first, last):
                offset = i - first
                
                # Save top element
                top = matrix[first][i]
                
                # Move left to top
                matrix[first][i] = matrix[last - offset][first]
                
                # Move bottom to left
                matrix[last - offset][first] = matrix[last][last - offset]
                
                # Move right to bottom
                matrix[last][last - offset] = matrix[i][last]
                
                # Move top to right
                matrix[i][last] = top

# Test the solution
solution = Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
solution.rotate(matrix1)
print(matrix1)  # Output: [[7,4,1],[8,5,2],[9,6,3]]

matrix2 = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
solution.rotate(matrix2)
print(matrix2)  # Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
