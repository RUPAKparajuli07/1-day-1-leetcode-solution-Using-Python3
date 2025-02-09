import random
from typing import List

class Solution:
    def __init__(self, nums: List[int]):
        self.indices = {}
        
        # Store all indices of each number in a dictionary
        for i, num in enumerate(nums):
            if num not in self.indices:
                self.indices[num] = []
            self.indices[num].append(i)

    def pick(self, target: int) -> int:
        # Randomly choose one of the stored indices
        return random.choice(self.indices[target])


# Example usage:
solution = Solution([1, 2, 3, 3, 3])
print(solution.pick(3))  # Output: Random index from [2, 3, 4]
print(solution.pick(1))  # Output: 0
print(solution.pick(3))  # Output: Random index from [2, 3, 4]
