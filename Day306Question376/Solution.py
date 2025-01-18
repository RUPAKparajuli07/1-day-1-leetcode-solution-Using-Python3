from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)
        
        # Initialize up and down
        up = 1
        down = 1
        
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                up = down + 1  # Increase length of wiggle ending in up
            elif nums[i] < nums[i - 1]:
                down = up + 1  # Increase length of wiggle ending in down
        
        # Maximum length will be the larger of up and down
        return max(up, down)
