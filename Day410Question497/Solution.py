import random
from bisect import bisect_left
from typing import List

class Solution:

    def __init__(self, rects: List[List[int]]):
        self.rects = rects
        self.prefix_sums = []
        total_points = 0
        for a, b, x, y in rects:
            count = (x - a + 1) * (y - b + 1)
            total_points += count
            self.prefix_sums.append(total_points)

    def pick(self) -> List[int]:
        # Pick a random point index
        point_index = random.randint(1, self.prefix_sums[-1])
        
        # Locate the rectangle using binary search
        rect_idx = bisect_left(self.prefix_sums, point_index)
        a, b, x, y = self.rects[rect_idx]
        
        # Number of points in this rectangle
        width = x - a + 1
        height = y - b + 1
        total_points_in_rect = width * height
        
        # Points before this rectangle
        prev_count = self.prefix_sums[rect_idx - 1] if rect_idx > 0 else 0
        index_in_rect = point_index - prev_count - 1
        
        # Convert index to coordinates
        dx = index_in_rect % width
        dy = index_in_rect // width
        return [a + dx, b + dy]
