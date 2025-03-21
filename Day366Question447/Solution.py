from typing import List
from collections import defaultdict

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        total_boomerangs = 0
        
        for i in range(len(points)):
            distance_map = defaultdict(int)
            
            for j in range(len(points)):
                if i == j:
                    continue  # Skip the same point
                
                # Calculate squared Euclidean distance
                dx = points[i][0] - points[j][0]
                dy = points[i][1] - points[j][1]
                dist = dx * dx + dy * dy
                
                # Update the count of distances
                distance_map[dist] += 1
            
            # Count valid boomerangs
            for count in distance_map.values():
                if count > 1:
                    total_boomerangs += count * (count - 1)  # Permutations P(m,2) = m * (m - 1)
        
        return total_boomerangs
