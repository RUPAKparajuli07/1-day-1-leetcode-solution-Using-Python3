from typing import List

class Solution:
    def findMinMoves(self, machines: List[int]) -> int:
        total = sum(machines)
        n = len(machines)
        
        # Step 1: Check if it's possible to balance
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        imbalance = 0
        
        # Step 2: Traverse machines to calculate max moves needed
        for load in machines:
            diff = load - target
            imbalance += diff
            max_moves = max(max_moves, abs(imbalance), diff)
        
        return max_moves
