import random
from typing import List

class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums[:]  # Store a copy of the original array
        self.nums = nums  # This is the array we will shuffle
    
    def reset(self) -> List[int]:
        # Return the original array
        return self.original
    
    def shuffle(self) -> List[int]:
        # Perform the Fisher-Yates shuffle
        for i in range(len(self.nums) - 1, 0, -1):
            j = random.randint(0, i)  # Choose a random index from 0 to i
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]  # Swap the elements
        return self.nums
