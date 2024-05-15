class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Initialize a 2D array to store the number of unique paths
        dp = [[0] * n for _ in range(m)]
        
        # Set the top-left cell to 1 since there's only one way to reach it
        dp[0][0] = 1
        
        # Fill the first row with 1s since the robot can only move right from the top row
        for i in range(1, n):
            dp[0][i] = 1
        
        # Fill the first column with 1s since the robot can only move down from the leftmost column
        for j in range(1, m):
            dp[j][0] = 1
        
        # Fill the rest of the cells using dynamic programming
        for i in range(1, m):
            for j in range(1, n):
                # The number of unique paths to reach cell (i, j) is the sum of
                # the number of unique paths to reach the cell above it and
                # the cell to its left
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        
        # Return the number of unique paths to reach the bottom-right corner
        return dp[m-1][n-1]

# Test the function
solution = Solution()
print(solution.uniquePaths(3, 7))  # Output: 28
print(solution.uniquePaths(3, 2))  # Output: 3
