class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # Create an empty set to store unique numbers
        seen = set()
        
        # Iterate through each number in the list
        for num in nums:
            # If the number is already in the set, return True (duplicate found)
            if num in seen:
                return True
            # Otherwise, add the number to the set
            seen.add(num)
        
        # If no duplicates found, return False
        return False
