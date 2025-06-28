from collections import defaultdict
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        current_sum = 0
        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1  # Base case for sum from beginning

        for num in nums:
            current_sum += num
            count += prefix_sums[current_sum - k]  # If (current_sum - k) seen before
            prefix_sums[current_sum] += 1

        return count
