import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # Min-heap for capital required (capital, profit)
        min_capital_heap = [(c, p) for c, p in zip(capital, profits)]
        heapq.heapify(min_capital_heap)
        
        # Max-heap for profits (we use negative to simulate max heap)
        max_profit_heap = []
        
        for _ in range(k):
            # Move all projects that can be started to max-profit heap
            while min_capital_heap and min_capital_heap[0][0] <= w:
                c, p = heapq.heappop(min_capital_heap)
                heapq.heappush(max_profit_heap, -p)
            
            # No projects we can afford to start
            if not max_profit_heap:
                break
            
            # Choose project with max profit
            w += -heapq.heappop(max_profit_heap)
        
        return w
