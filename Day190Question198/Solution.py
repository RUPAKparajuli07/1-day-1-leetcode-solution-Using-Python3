from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Base cases: if there are no houses or only one house
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        # Initialize dp array to store the maximum money that can be robbed up to each house
        dp = [0] * len(nums)
        
        # First house can only rob itself
        dp[0] = nums[0]
        
        # Second house: rob either the first or the second house, whichever has more money
        dp[1] = max(nums[0], nums[1])
        
        # Fill dp array by following the recurrence relation
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        
        # The last element of dp will contain the maximum amount that can be robbed
        return dp[-1]
