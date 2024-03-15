from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create a dictionary to store elements and their indices
        num_indices = {}
        
        # Iterate through the array
        for i, num in enumerate(nums):
            # Check if the complement of the current number exists in the dictionary
            complement = target - num
            if complement in num_indices:
                # If found, return the indices of both numbers
                return [num_indices[complement], i]
            # Otherwise, store the current number and its index in the dictionary
            num_indices[num] = i
        
        # If no solution is found, return an empty list
        return []
