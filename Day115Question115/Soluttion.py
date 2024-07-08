class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        # Lengths of the strings
        m, n = len(s), len(t)
        
        # Create a 2D DP array with (m+1) x (n+1)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initializing the first column, as an empty t is a subsequence of any string s
        for i in range(m + 1):
            dp[i][0] = 1
        
        # Fill the DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s[i - 1] == t[j - 1]:
                    dp[i][j] = dp[i - 1][j] + dp[i - 1][j - 1]
                else:
                    dp[i][j] = dp[i - 1][j]
        
        # The answer is in the bottom-right cell
        return dp[m][n]

# Example usage:
# solution = Solution()
# print(solution.numDistinct("rabbbit", "rabbit"))  # Output: 3
# print(solution.numDistinct("babgbag", "bag"))     # Output: 5
