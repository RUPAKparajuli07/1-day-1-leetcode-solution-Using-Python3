class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Initialize pointers for current element (current), red (low), and blue (high)
        low, high = 0, len(nums) - 1
        current = 0
        
        # Traverse the array
        while current <= high:
            if nums[current] == 0:
                # Swap the current element with the low pointer element
                nums[current], nums[low] = nums[low], nums[current]
                # Increment both current and low pointers
                low += 1
                current += 1
            elif nums[current] == 2:
                # Swap the current element with the high pointer element
                nums[current], nums[high] = nums[high], nums[current]
                # Decrement the high pointer
                high -= 1
            else:
                # Move to the next element if the current element is 1
                current += 1
