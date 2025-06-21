class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        # dp[i]: number of valid strings of length i with no 'A' and no "LLL"
        dp = [0] * (n + 3)
        dp[0], dp[1], dp[2] = 1, 2, 4  # "", "P/L", "PP/PL/LP/LL"

        for i in range(3, n + 1):
            dp[i] = (dp[i - 1] + dp[i - 2] + dp[i - 3]) % MOD

        total = dp[n]  # All strings with 0 'A'

        # Add combinations with exactly 1 'A'
        for i in range(n):
            left = dp[i]          # valid strings of length i (before 'A')
            right = dp[n - 1 - i] # valid strings of length n-1-i (after 'A')
            total = (total + (left * right) % MOD) % MOD

        return total
