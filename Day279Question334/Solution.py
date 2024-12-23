class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        first = float('inf')  # The smallest number seen so far
        second = float('inf') # The second smallest number seen so far
        
        for num in nums:
            if num <= first:
                first = num  # Update the smallest number
            elif num <= second:
                second = num  # Update the second smallest number
            else:
                # If we find a number larger than both `first` and `second`, we have found a triplet
                return True
        
        return False  # No triplet found
