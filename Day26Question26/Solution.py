from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Initialize pointer for unique elements
        j = 1
        
        # Iterate through the array starting from the second element
        for i in range(1, len(nums)):
            # If current element is different from previous unique element
            if nums[i] != nums[j - 1]:
                # Move the current element to the position of the next unique element
                nums[j] = nums[i]
                # Increment the unique element pointer
                j += 1
        
        # Return the number of unique elements
        return j

# Example usage:
solution = Solution()
nums1 = [1, 1, 2]
print(solution.removeDuplicates(nums1))  # Output: 2, nums = [1, 2, _]

nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
print(solution.removeDuplicates(nums2))  # Output: 5, nums = [0, 1, 2, 3, 4, _, _, _, _, _]
