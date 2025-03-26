from typing import List

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        # Step 1: Sort by end points
        points.sort(key=lambda x: x[1])

        arrows = 1  # At least one arrow is needed
        prev_end = points[0][1]  # First balloon's end

        # Step 2: Traverse through sorted balloons
        for start, end in points[1:]:
            if start > prev_end:  # Need a new arrow
                arrows += 1
                prev_end = end  # Update the new end

        return arrows
