from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        n = len(prices)
        hold, sold, rest = [0] * n, [0] * n, [0] * n
        
        # Initial states
        hold[0] = -prices[0]  # Buy the stock on day 0
        sold[0] = 0           # Cannot sell on day 0
        rest[0] = 0           # No profit if resting on day 0
        
        for i in range(1, n):
            hold[i] = max(hold[i-1], rest[i-1] - prices[i])
            sold[i] = hold[i-1] + prices[i]
            rest[i] = max(rest[i-1], sold[i-1])
        
        # Maximum profit will be max(sold[n-1], rest[n-1])
        return max(sold[-1], rest[-1])
