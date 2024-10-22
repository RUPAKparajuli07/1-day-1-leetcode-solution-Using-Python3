from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # List to store the ranges
        ranges = []
        
        # Edge case: empty array
        if not nums:
            return ranges
        
        # Start of the current range
        start = nums[0]
        
        # Traverse through the numbers in the list
        for i in range(1, len(nums)):
            # Check if the current number is not consecutive
            if nums[i] != nums[i - 1] + 1:
                # If the start and current are different, it's a range, otherwise it's a single number
                if start != nums[i - 1]:
                    ranges.append(f"{start}->{nums[i - 1]}")
                else:
                    ranges.append(f"{start}")
                # Update the start of the next range
                start = nums[i]
        
        # Handle the last range after the loop
        if start != nums[-1]:
            ranges.append(f"{start}->{nums[-1]}")
        else:
            ranges.append(f"{start}")
        
        return ranges
