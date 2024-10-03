from typing import List

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # Initialize the window pointers and variables
        start = 0
        sum_ = 0
        min_length = float('inf')  # Start with an infinitely large value
        
        # Traverse the array with the end pointer
        for end in range(len(nums)):
            sum_ += nums[end]  # Add current number to the window's sum
            
            # Try to shrink the window as much as possible while the sum is valid
            while sum_ >= target:
                min_length = min(min_length, end - start + 1)  # Update min length
                sum_ -= nums[start]  # Remove the leftmost element from sum
                start += 1  # Move the start pointer right
                
        # If no valid subarray was found, return 0; else, return the minimal length
        return min_length if min_length != float('inf') else 0
