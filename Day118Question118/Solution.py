from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result list with the first row of Pascal's triangle
        triangle = [[1]]
        
        # Generate each row of Pascal's triangle
        for i in range(1, numRows):
            # Start the row with a 1
            row = [1]
            # Get the previous row from the triangle
            prev_row = triangle[i-1]
            
            # Each element in the middle of the row is the sum of the two elements above it
            for j in range(1, i):
                row.append(prev_row[j-1] + prev_row[j])
            
            # End the row with a 1
            row.append(1)
            # Add the generated row to the triangle
            triangle.append(row)
        
        return triangle

# Example usage:
solution = Solution()
print(solution.generate(5))
print(solution.generate(1))
