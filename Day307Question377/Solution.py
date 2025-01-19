from typing import List

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        # Initialize the dp array with 0s, with size (target + 1)
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case
        
        # Iterate for all target values from 1 to target
        for i in range(1, target + 1):
            for num in nums:
                if i - num >= 0:
                    dp[i] += dp[i - num]
        
        return dp[target]
