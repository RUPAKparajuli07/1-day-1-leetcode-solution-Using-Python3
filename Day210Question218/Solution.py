import heapq
from typing import List

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # List of all events
        events = []
        for left, right, height in buildings:
            # Starting point of the building, we use -height to distinguish from the end points
            events.append((left, -height, right))
            # Ending point of the building
            events.append((right, 0, 0))
        
        # Sort events: First by x, then by height (for start events), and finally by end events
        events.sort()
        
        # Result list and max-heap to store active buildings
        result = []
        max_heap = [(0, float('inf'))]  # Initial height of 0 for the ground
        
        for x, neg_height, end in events:
            # Remove buildings from the heap whose right edge is less than or equal to the current x
            while max_heap[0][1] <= x:
                heapq.heappop(max_heap)
            
            # If it's a start of a building (neg_height < 0), add it to the heap
            if neg_height != 0:
                heapq.heappush(max_heap, (neg_height, end))
            
            # If the max height changes, add the point to the result
            if not result or result[-1][1] != -max_heap[0][0]:
                result.append([x, -max_heap[0][0]])
        
        return result
