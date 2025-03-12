from typing import List
import bisect

class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        # Step 1: Store (start, index) and sort by start value
        sorted_intervals = sorted((interval[0], i) for i, interval in enumerate(intervals))
        starts = [x[0] for x in sorted_intervals]  # Extract sorted start values
        
        result = []
        
        # Step 2: Find the right interval using binary search
        for _, end in intervals:
            idx = bisect.bisect_left(starts, end)  # Find the smallest start >= end
            
            if idx < len(starts):  # Valid right interval found
                result.append(sorted_intervals[idx][1])
            else:  # No valid right interval
                result.append(-1)
        
        return result
