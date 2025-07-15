from typing import List

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the list
        max_sum = 0
        for i in range(0, len(nums), 2):  # Step 2: Take every alternate (even index)
            max_sum += nums[i]  # Step 3: Add the smaller number of each pair
        return max_sum
