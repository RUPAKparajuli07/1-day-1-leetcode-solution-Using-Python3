from typing import List

class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        n = len(distance)
        for i in range(3, n):
            # Case 1: Crosses the segment 2 steps behind
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            
            # Case 2: Crosses the segment 4 steps behind
            if i >= 4 and distance[i-1] == distance[i-3] and distance[i] + distance[i-4] >= distance[i-2]:
                return True
            
            # Case 3: Crosses the segment 5 steps behind
            if i >= 5 and distance[i-2] > distance[i-4] and distance[i] + distance[i-4] >= distance[i-2] and distance[i-1] <= distance[i-3] and distance[i-1] + distance[i-5] >= distance[i-3]:
                return True
        
        return False
