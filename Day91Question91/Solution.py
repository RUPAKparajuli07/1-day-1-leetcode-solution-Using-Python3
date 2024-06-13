class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        
        for i in range(2, n + 1):
            single_digit = int(s[i-1])
            double_digit = int(s[i-2:i])
            
            if 1 <= single_digit <= 9:
                dp[i] += dp[i-1]
            
            if 10 <= double_digit <= 26:
                dp[i] += dp[i-2]
        
        return dp[n]

# Example usage:
solution = Solution()
print(solution.numDecodings("12"))  # Output: 2
print(solution.numDecodings("226")) # Output: 3
print(solution.numDecodings("06"))  # Output: 0
