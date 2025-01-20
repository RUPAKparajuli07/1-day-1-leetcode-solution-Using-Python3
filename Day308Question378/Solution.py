from typing import List

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)

        # Helper function to count elements <= target
        def count_less_equal(mid):
            count, row, col = 0, n - 1, 0
            while row >= 0 and col < n:
                if matrix[row][col] <= mid:
                    # All elements in this row up to 'col' are <= mid
                    count += (row + 1)
                    col += 1
                else:
                    # Move to the next smaller row
                    row -= 1
            return count

        # Binary search on the value range
        low, high = matrix[0][0], matrix[-1][-1]
        while low < high:
            mid = (low + high) // 2
            if count_less_equal(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
