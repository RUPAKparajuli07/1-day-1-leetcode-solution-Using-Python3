from typing import List

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Initialize dp array with amount+1 size
        dp = [0] * (amount + 1)
        dp[0] = 1  # One way to make amount 0
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
