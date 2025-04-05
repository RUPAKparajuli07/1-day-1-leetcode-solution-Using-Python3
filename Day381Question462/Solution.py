from typing import List

class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()  # Step 1: Sort the array
        median = nums[len(nums) // 2]  # Step 2: Get the median
        return sum(abs(num - median) for num in nums)  # Step 3 & 4
