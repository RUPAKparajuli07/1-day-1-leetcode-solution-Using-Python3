class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        # Create a 2D DP array
        dp = [[0] * n for _ in range(n)]

        # Single characters are palindromes of length 1
        for i in range(n):
            dp[i][i] = 1

        # Fill the table for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1] if i + 1 <= j - 1 else 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        # Final result is the longest palindromic subsequence from 0 to n-1
        return dp[0][n - 1]
