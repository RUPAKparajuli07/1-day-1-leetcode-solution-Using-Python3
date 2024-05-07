from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []

        result = []
        row_begin, row_end = 0, len(matrix) - 1
        col_begin, col_end = 0, len(matrix[0]) - 1

        while row_begin <= row_end and col_begin <= col_end:
            # Traverse right
            for i in range(col_begin, col_end + 1):
                result.append(matrix[row_begin][i])
            row_begin += 1

            # Traverse down
            for i in range(row_begin, row_end + 1):
                result.append(matrix[i][col_end])
            col_end -= 1

            # Traverse left
            if row_begin <= row_end:
                for i in range(col_end, col_begin - 1, -1):
                    result.append(matrix[row_end][i])
                row_end -= 1

            # Traverse up
            if col_begin <= col_end:
                for i in range(row_end, row_begin - 1, -1):
                    result.append(matrix[i][col_begin])
                col_begin += 1

        return result

# Example usage:
sol = Solution()
matrix1 = [[1,2,3],[4,5,6],[7,8,9]]
print(sol.spiralOrder(matrix1))  # Output: [1,2,3,6,9,8,7,4,5]

matrix2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(sol.spiralOrder(matrix2))  # Output: [1,2,3,4,8,12,11,10,9,5,6,7]
