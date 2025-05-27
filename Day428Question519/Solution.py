import random
from typing import List

class Solution:

    def __init__(self, m: int, n: int):
        self.m = m
        self.n = n
        self.total = m * n
        self.map = {}  # Tracks the position mapping
        self.available = self.total  # Remaining zero positions

    def flip(self) -> List[int]:
        rand_idx = random.randint(0, self.available - 1)

        # Get the actual position to flip
        actual = self.map.get(rand_idx, rand_idx)

        # Update the map: simulate swapping rand_idx with last available index
        self.available -= 1
        self.map[rand_idx] = self.map.get(self.available, self.available)

        # Convert 1D index back to 2D coordinates
        return [actual // self.n, actual % self.n]

    def reset(self) -> None:
        self.map.clear()
        self.available = self.total
