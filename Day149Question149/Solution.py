from collections import defaultdict
from typing import List
import math

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def slope(p1, p2):
            dy = p2[1] - p1[1]
            dx = p2[0] - p1[0]
            if dx == 0:
                return (float('inf'), 0)  # vertical line
            if dy == 0:
                return (0, 0)  # horizontal line
            g = gcd(dy, dx)
            return (dy // g, dx // g)

        n = len(points)
        if n <= 1:
            return n

        max_points = 1

        for i in range(n):
            slopes = defaultdict(int)
            duplicate = 1
            for j in range(i + 1, n):
                if points[i] == points[j]:
                    duplicate += 1
                else:
                    sl = slope(points[i], points[j])
                    slopes[sl] += 1
            
            max_points = max(max_points, max(slopes.values(), default=0) + duplicate)

        return max_points
