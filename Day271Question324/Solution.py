from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Reorder the array nums to satisfy the wiggle sort condition.
        """
        # Step 1: Sort the array
        nums.sort()
        
        # Step 2: Find the middle of the array
        n = len(nums)
        mid = (n - 1) // 2  # Median index
        
        # Step 3: Split into two halves and reverse
        smaller = nums[:mid + 1][::-1]  # First half (smaller elements)
        larger = nums[mid + 1:][::-1]   # Second half (larger elements)
        
        # Step 4: Reorder using virtual indexing
        for i in range(n):
            if i % 2 == 0:
                nums[i] = smaller.pop(0)  # Fill even indices with smaller values
            else:
                nums[i] = larger.pop(0)   # Fill odd indices with larger values
