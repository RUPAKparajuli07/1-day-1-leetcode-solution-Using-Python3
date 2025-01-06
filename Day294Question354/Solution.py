from typing import List
import bisect

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        # Step 1: Sort envelopes by width (ascending) and height (descending for same width)
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        
        # Step 2: Extract the heights and find the LIS
        heights = [envelope[1] for envelope in envelopes]
        lis = []  # This will store the LIS
        
        for height in heights:
            # Use binary search to find the position to replace or extend
            pos = bisect.bisect_left(lis, height)
            if pos == len(lis):
                lis.append(height)  # Add to the LIS if it is larger than all current elements
            else:
                lis[pos] = height  # Replace the existing element to maintain the LIS
        
        return len(lis)
