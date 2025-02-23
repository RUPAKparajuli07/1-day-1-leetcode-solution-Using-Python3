from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0
        
        # Variable to store the total number of arithmetic slices
        total_slices = 0
        
        # Variable to store the length of the current arithmetic slice
        current_slices = 0
        
        for i in range(2, n):
            # Check if the difference between nums[i] and nums[i-1] is the same as nums[i-1] and nums[i-2]
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                # If they match, increment current_slices
                current_slices += 1
                # Add current_slices to total_slices
                total_slices += current_slices
            else:
                # Reset the current_slices if they don't match
                current_slices = 0
        
        return total_slices
