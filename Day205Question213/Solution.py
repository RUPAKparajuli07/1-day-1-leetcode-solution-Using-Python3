from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        # Helper function to calculate the max money can be robbed in a linear arrangement
        def rob_linear(nums: List[int]) -> int:
            n = len(nums)
            if n == 0:
                return 0
            if n == 1:
                return nums[0]
            
            dp = [0] * n
            dp[0] = nums[0]
            dp[1] = max(nums[0], nums[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2] + nums[i])
                
            return dp[-1]
        
        n = len(nums)
        if n == 1:
            return nums[0]
        
        # Rob houses from 0 to n-2 or from 1 to n-1 and take the max
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
