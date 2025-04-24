from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_count = 0  # To store the maximum number of consecutive 1s
        count = 0      # To store the current streak of 1s

        for num in nums:
            if num == 1:
                count += 1
                max_count = max(max_count, count)
            else:
                count = 0  # Reset the count when we see a 0

        return max_count
