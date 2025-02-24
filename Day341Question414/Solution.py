from typing import List

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Step 1: Use a set to store distinct numbers
        distinct_nums = set(nums)
        
        # Step 2: Sort the distinct numbers in descending order
        sorted_nums = sorted(distinct_nums, reverse=True)
        
        # Step 3: Return the third distinct maximum or the maximum if less than 3 distinct numbers
        if len(sorted_nums) >= 3:
            return sorted_nums[2]  # Third maximum
        else:
            return sorted_nums[0]  # Maximum if less than 3 distinct numbers
