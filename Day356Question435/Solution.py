from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals based on end times
        intervals.sort(key=lambda x: x[1])
        
        count = 0  # Count of intervals to remove
        prev_end = float('-inf')  # Previous non-overlapping interval end
        
        for start, end in intervals:
            if start >= prev_end:  # If no overlap
                prev_end = end  # Update the end of last non-overlapping interval
            else:  # If overlapping, remove the interval
                count += 1  
        
        return count
