from typing import List

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Add virtual balloons with value 1 at both ends
        nums = [1] + nums + [1]
        n = len(nums)
        
        # DP table initialization
        dp = [[0] * n for _ in range(n)]
        
        # Fill DP table
        for length in range(2, n):  # length of the range [left, right]
            for left in range(n - length):  # left boundary of the range
                right = left + length  # right boundary of the range
                # Calculate max coins for dp[left][right]
                for i in range(left + 1, right):  # i is the last balloon to burst
                    dp[left][right] = max(
                        dp[left][right],
                        nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right]
                    )
        
        # The result is the max coins for bursting all balloons in the range [0, n-1]
        return dp[0][n - 1]
