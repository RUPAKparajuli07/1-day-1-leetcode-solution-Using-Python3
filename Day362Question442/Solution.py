from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        duplicates = []
        
        for num in nums:
            index = abs(num) - 1  # Get index (1-based to 0-based)
            
            if nums[index] < 0:  # If already marked negative, it's a duplicate
                duplicates.append(abs(num))
            else:
                nums[index] = -nums[index]  # Mark as visited by making negative
        
        return duplicates
