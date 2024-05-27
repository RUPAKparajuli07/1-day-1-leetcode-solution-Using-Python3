class Solution:
    def searchMatrix(self, matrix, target):
        # Check if the matrix is empty
        if not matrix or not matrix[0]:
            return False

        # Get the dimensions of the matrix
        m, n = len(matrix), len(matrix[0])

        # Initialize the binary search bounds
        left, right = 0, m * n - 1

        # Perform binary search
        while left <= right:
            # Calculate the mid index
            mid = (left + right) // 2
            
            # Convert mid index to 2D matrix coordinates
            mid_value = matrix[mid // n][mid % n]

            # Compare the mid value with the target
            if mid_value == target:
                return True  # Target found
            elif mid_value < target:
                left = mid + 1  # Search in the right half
            else:
                right = mid - 1  # Search in the left half

        # Target not found in the matrix
        return False

# Example usage
solution = Solution()
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3
print(solution.searchMatrix(matrix, target))  # Output: True

target = 13
print(solution.searchMatrix(matrix, target))  # Output: False
