class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # Create a DP table
        dp = [[0] * (n + 1) for _ in range(n + 1)]
        
        # Fill the DP table for ranges of increasing lengths
        for length in range(2, n + 1):  # Length of range
            for i in range(1, n - length + 2):  # Starting point
                j = i + length - 1  # Ending point
                dp[i][j] = float('inf')
                # Consider all possible guesses within the range
                for k in range(i, j + 1):
                    # Calculate cost of guessing `k`
                    cost = k + max(dp[i][k-1] if k > i else 0, dp[k+1][j] if k < j else 0)
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[1][n]
