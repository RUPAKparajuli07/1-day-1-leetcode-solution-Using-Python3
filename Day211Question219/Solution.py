class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # Dictionary to store the last seen index of each element
        index_map = {}
        
        # Iterate over the array
        for i, num in enumerate(nums):
            # If the number has been seen before and the difference between indices is <= k
            if num in index_map and i - index_map[num] <= k:
                return True
            # Update the index of the current number
            index_map[num] = i
        
        # If no duplicates within range are found
        return False
