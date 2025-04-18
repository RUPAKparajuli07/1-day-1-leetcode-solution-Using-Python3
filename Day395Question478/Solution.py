import random
import math
from typing import List

class Solution:

    def __init__(self, radius: float, x_center: float, y_center: float):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> List[float]:
        angle = random.uniform(0, 2 * math.pi)  # Random angle in radians
        r = math.sqrt(random.uniform(0, 1)) * self.radius  # Random radius with uniform distribution
        x = self.x_center + r * math.cos(angle)
        y = self.y_center + r * math.sin(angle)
        return [x, y]
