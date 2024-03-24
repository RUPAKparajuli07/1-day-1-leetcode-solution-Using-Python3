class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Dynamic programming table
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        
        # Empty string and empty pattern match
        dp[0][0] = True
        
        # Handling patterns with '*' as the first character
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 2]
        
        # Filling up the dynamic programming table
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '.' or p[j - 1] == s[i - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        
        return dp[len(s)][len(p)]

# Example usage:
solution = Solution()
print(solution.isMatch("aa", "a"))    # Output: false
print(solution.isMatch("aa", "a*"))   # Output: true
print(solution.isMatch("ab", ".*"))   # Output: true
