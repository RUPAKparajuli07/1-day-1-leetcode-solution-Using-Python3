class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Moves all 0's to the end of nums while maintaining the relative order
        of the non-zero elements.
        
        Args:
        nums (List[int]): The input list of integers.

        Returns:
        None: Modifies nums in-place.
        """
        # Pointer to track the position of the next non-zero element
        non_zero_index = 0
        
        # Iterate through the list
        for i in range(len(nums)):
            # If the current element is non-zero, place it at the non_zero_index
            if nums[i] != 0:
                nums[non_zero_index], nums[i] = nums[i], nums[non_zero_index]
                non_zero_index += 1
