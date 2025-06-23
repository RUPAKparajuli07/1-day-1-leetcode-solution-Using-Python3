from collections import defaultdict
from typing import List

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_counts = defaultdict(int)

        for row in wall:
            edge_position = 0
            # Exclude the last brick to avoid the right edge
            for brick in row[:-1]:
                edge_position += brick
                edge_counts[edge_position] += 1

        # If no edges were found, that means the line crosses all rows
        max_edges = max(edge_counts.values(), default=0)
        return len(wall) - max_edges
