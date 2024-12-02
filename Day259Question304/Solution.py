from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        if not matrix or not matrix[0]:
            self.prefix_sum = []
            return
        
        rows, cols = len(matrix), len(matrix[0])
        # Create a prefix sum matrix
        self.prefix_sum = [[0] * cols for _ in range(rows)]
        
        # Compute prefix sums
        for i in range(rows):
            for j in range(cols):
                self.prefix_sum[i][j] = matrix[i][j]
                if i > 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i-1][j]
                if j > 0:
                    self.prefix_sum[i][j] += self.prefix_sum[i][j-1]
                if i > 0 and j > 0:
                    self.prefix_sum[i][j] -= self.prefix_sum[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        # Use the prefix sum matrix to compute the region sum
        total = self.prefix_sum[row2][col2]
        if row1 > 0:
            total -= self.prefix_sum[row1-1][col2]
        if col1 > 0:
            total -= self.prefix_sum[row2][col1-1]
        if row1 > 0 and col1 > 0:
            total += self.prefix_sum[row1-1][col1-1]
        return total
