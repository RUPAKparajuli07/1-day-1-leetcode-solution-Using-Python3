import random
from bisect import bisect_left
from typing import List

class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sums = []
        curr_sum = 0
        for weight in w:
            curr_sum += weight
            self.prefix_sums.append(curr_sum)
        self.total_sum = curr_sum

    def pickIndex(self) -> int:
        target = random.randint(1, self.total_sum)
        return bisect_left(self.prefix_sums, target)
