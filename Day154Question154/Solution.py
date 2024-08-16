from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = (left + right) // 2
            
            # If the middle element is less than the rightmost element,
            # the smallest value is in the left half or could be mid itself.
            if nums[mid] < nums[right]:
                right = mid
            # If the middle element is greater than the rightmost element,
            # the smallest value is in the right half.
            elif nums[mid] > nums[right]:
                left = mid + 1
            else:
                # If nums[mid] == nums[right], we can't determine the smallest
                # value's location, so reduce the search space by decreasing right.
                right -= 1
        
        # After the loop, left should point to the minimum value
        return nums[left]
