from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the next element, move left
            if nums[mid] > nums[mid + 1]:
                right = mid
            else:
                # Otherwise, move right
                left = mid + 1
        
        # At the end of the loop, left == right, which points to the peak element
        return left
