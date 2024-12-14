from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # Initialize dp array with infinity
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0  # Base case: 0 coins needed to make amount 0
        
        # Fill dp array
        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        # If dp[amount] is inf, it's not possible to make that amount
        return dp[amount] if dp[amount] != float('inf') else -1
