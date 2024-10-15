from typing import List

class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        # Edge case: if matrix is empty, return 0
        if not matrix or not matrix[0]:
            return 0
        
        # Initialize dimensions
        m, n = len(matrix), len(matrix[0])
        
        # DP table to store the side length of the largest square ending at each point
        dp = [[0] * n for _ in range(m)]
        
        max_side = 0  # To track the maximum square side length found
        
        # Iterate through the matrix
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '1':
                    if i == 0 or j == 0:
                        # For the first row or first column, the value in dp is same as matrix
                        dp[i][j] = 1
                    else:
                        # Calculate the size of the square that can be formed
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    # Update the maximum side length
                    max_side = max(max_side, dp[i][j])
        
        # The area of the largest square is side length squared
        return max_side * max_side
