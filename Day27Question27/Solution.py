from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Initialize a pointer to keep track of non-val elements
        k = 0
        
        # Iterate through the array
        for i in range(len(nums)):
            # If current element is not equal to val, move it to the position k
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        
        # k represents the number of elements in nums which are not equal to val
        return k
