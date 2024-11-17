class Solution:
    def numSquares(self, n: int) -> int:
        # Step 1: Initialize a DP array where dp[i] represents the minimum number of perfect squares to sum to i
        dp = [float('inf')] * (n + 1)
        dp[0] = 0  # Base case: 0 can be represented with 0 perfect squares

        # Step 2: Precompute all perfect squares less than or equal to n
        squares = []
        for i in range(1, int(n**0.5) + 1):
            squares.append(i * i)

        # Step 3: Fill the DP array
        for i in range(1, n + 1):
            for square in squares:
                if i < square:  # If the square is greater than i, break
                    break
                dp[i] = min(dp[i], dp[i - square] + 1)  # Transition step
        
        return dp[n]  # Return the minimum number of perfect squares to sum to n
