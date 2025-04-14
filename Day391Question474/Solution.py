from typing import List

class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        # Initialize dp array
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            zero = s.count('0')  # Count of 0's in the string
            one = s.count('1')   # Count of 1's in the string

            # Update dp table in reverse to avoid reusing the same string
            for i in range(m, zero - 1, -1):
                for j in range(n, one - 1, -1):
                    dp[i][j] = max(dp[i][j], dp[i - zero][j - one] + 1)

        return dp[m][n]
