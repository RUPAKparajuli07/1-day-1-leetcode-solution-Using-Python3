from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count_index_map = {0: -1}  # map from running sum to first index it was seen
        max_length = 0
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += 1 if num == 1 else -1

            if running_sum in count_index_map:
                max_length = max(max_length, i - count_index_map[running_sum])
            else:
                count_index_map[running_sum] = i

        return max_length
