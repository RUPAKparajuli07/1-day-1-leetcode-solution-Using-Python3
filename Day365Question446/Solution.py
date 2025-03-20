from collections import defaultdict
from typing import List

class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [defaultdict(int) for _ in range(n)]
        total_count = 0
        
        for i in range(n):
            for j in range(i):
                diff = nums[i] - nums[j]
                count = dp[j][diff]
                
                dp[i][diff] += count + 1
                total_count += count  # Only sequences of length ≥ 3 are counted
                
        return total_count
