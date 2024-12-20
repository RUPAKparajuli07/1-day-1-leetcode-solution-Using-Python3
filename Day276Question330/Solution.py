from typing import List

class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        max_reachable = 0
        index = 0
        
        # Iterate while the range [1, n] is not fully covered
        while max_reachable < n:
            if index < len(nums) and nums[index] <= max_reachable + 1:
                # Extend the coverage using the current number
                max_reachable += nums[index]
                index += 1
            else:
                # Patch with max_reachable + 1 to cover the gap
                patches += 1
                max_reachable += max_reachable + 1
        
        return patches
