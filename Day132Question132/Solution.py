class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        
        # Create a 2D array to store palindrome information
        is_palindrome = [[False] * n for _ in range(n)]
        
        # Initialize is_palindrome array
        for i in range(n):
            is_palindrome[i][i] = True  # Single character substrings are palindromes
        
        for length in range(2, n + 1):  # length of substring
            for start in range(n - length + 1):
                end = start + length - 1
                if length == 2:
                    is_palindrome[start][end] = (s[start] == s[end])
                else:
                    is_palindrome[start][end] = (s[start] == s[end]) and is_palindrome[start + 1][end - 1]
        
        # Initialize the dp array
        dp = [0] * n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = i
                for j in range(1, i + 1):
                    if is_palindrome[j][i]:
                        dp[i] = min(dp[i], dp[j - 1] + 1)
        
        return dp[-1]

# Example usage
sol = Solution()
print(sol.minCut("aab"))  # Output: 1
print(sol.minCut("a"))    # Output: 0
print(sol.minCut("ab"))   # Output: 1
