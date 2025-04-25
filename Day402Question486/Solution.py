from typing import List
from functools import lru_cache

class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        
        # Memoization to avoid recomputation
        @lru_cache(None)
        def dp(left: int, right: int) -> int:
            # Base case: only one element left
            if left == right:
                return nums[left]
            
            # Choose left or right, subtract opponent's best response
            pick_left = nums[left] - dp(left + 1, right)
            pick_right = nums[right] - dp(left, right - 1)
            
            return max(pick_left, pick_right)

        # If player1 can get a non-negative score difference, they can win or draw
        return dp(0, len(nums) - 1) >= 0
