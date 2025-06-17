from functools import lru_cache
from typing import List

class Solution:
    def removeBoxes(self, boxes: List[int]) -> int:
        n = len(boxes)
        
        @lru_cache(None)
        def dp(l, r, k):
            if l > r:
                return 0
            
            # Merge boxes of the same color at the end
            while l < r and boxes[r] == boxes[r-1]:
                r -= 1
                k += 1
            
            # Case 1: Remove the last group directly
            res = dp(l, r - 1, 0) + (k + 1) * (k + 1)
            
            # Case 2: Try merging non-adjacent same colored boxes
            for i in range(l, r):
                if boxes[i] == boxes[r]:
                    res = max(res, dp(l, i, k + 1) + dp(i + 1, r - 1, 0))
            
            return res
        
        return dp(0, n - 1, 0)
