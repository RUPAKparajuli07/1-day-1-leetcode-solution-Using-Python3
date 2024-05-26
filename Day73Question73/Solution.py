class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        if not matrix:
            return
        
        m, n = len(matrix), len(matrix[0])
        
        # Step 1: Determine if the first row or first column needs to be zeroed
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_column_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Step 2: Use the first row and column to mark zero rows and columns
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Step 3: Zero out cells based on markers in the first row and column
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Step 4: Zero out the first row if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        
        # Step 5: Zero out the first column if needed
        if first_column_zero:
            for i in range(m):
                matrix[i][0] = 0
