from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        # Start from the second last row and move upwards
        for row in range(len(triangle) - 2, -1, -1):
            for col in range(len(triangle[row])):
                # Update the current value to the minimum path sum of the adjacent numbers in the row below
                triangle[row][col] += min(triangle[row + 1][col], triangle[row + 1][col + 1])
        
        # The top element will contain the minimum path sum
        return triangle[0][0]

# Example usage
solution = Solution()
print(solution.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]))  # Output: 11
print(solution.minimumTotal([[-10]]))  # Output: -10
