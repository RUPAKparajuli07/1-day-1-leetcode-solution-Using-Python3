from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            # Make sure mid is even for comparison with mid+1
            if mid % 2 == 1:
                mid -= 1
            # If pair is valid, move right
            if nums[mid] == nums[mid + 1]:
                low = mid + 2
            else:
                high = mid
                
        return nums[low]
