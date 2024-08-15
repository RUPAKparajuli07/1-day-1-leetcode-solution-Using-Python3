from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is greater than the rightmost element, 
            # the minimum is in the right half
            if nums[mid] > nums[right]:
                left = mid + 1
            # If the middle element is less than or equal to the rightmost element, 
            # the minimum is in the left half or is the middle element itself
            else:
                right = mid
        
        # When left == right, that's the minimum element
        return nums[left]
