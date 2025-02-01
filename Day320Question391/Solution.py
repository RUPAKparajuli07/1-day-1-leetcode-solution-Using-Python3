from typing import List

class Solution:
    def isRectangleCover(self, rectangles: List[List[int]]) -> bool:
        corner_set = set()
        area_sum = 0
        
        min_x, min_y = float('inf'), float('inf')
        max_x, max_y = float('-inf'), float('-inf')
        
        for x1, y1, x2, y2 in rectangles:
            # Calculate total area
            area_sum += (x2 - x1) * (y2 - y1)
            
            # Update bounding rectangle
            min_x, min_y = min(min_x, x1), min(min_y, y1)
            max_x, max_y = max(max_x, x2), max(max_y, y2)
            
            # Process corners
            for corner in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
                if corner in corner_set:
                    corner_set.remove(corner)
                else:
                    corner_set.add(corner)

        # Compute expected area of the bounding rectangle
        expected_area = (max_x - min_x) * (max_y - min_y)

        # Check conditions:
        return (
            area_sum == expected_area and
            len(corner_set) == 4 and
            (min_x, min_y) in corner_set and
            (min_x, max_y) in corner_set and
            (max_x, min_y) in corner_set and
            (max_x, max_y) in corner_set
        )
