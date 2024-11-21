from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: Detecting the cycle
        tortoise = nums[0]
        hare = nums[0]
        
        while True:
            tortoise = nums[tortoise]  # Move one step
            hare = nums[nums[hare]]   # Move two steps
            if tortoise == hare:      # Intersection point
                break

        # Phase 2: Finding the entrance to the cycle
        tortoise = nums[0]            # Reset one pointer to the start
        while tortoise != hare:
            tortoise = nums[tortoise] # Move one step
            hare = nums[hare]         # Move one step

        return hare
