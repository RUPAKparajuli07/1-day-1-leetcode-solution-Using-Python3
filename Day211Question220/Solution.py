from sortedcontainers import SortedList

class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        # Use a sorted list to keep track of the sliding window of elements
        sorted_list = SortedList()
        
        for i in range(len(nums)):
            # Remove the element that is out of the sliding window
            if i > indexDiff:
                sorted_list.remove(nums[i - indexDiff - 1])
            
            # Find the potential position where nums[i] could be placed in the sorted list
            pos = SortedList.bisect_left(sorted_list, nums[i] - valueDiff)
            
            # Check if the element within range of valueDiff exists
            if pos < len(sorted_list) and abs(sorted_list[pos] - nums[i]) <= valueDiff:
                return True
            
            # Add the current element to the sorted list
            sorted_list.add(nums[i])
        
        return False
