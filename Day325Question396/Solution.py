from typing import List

class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        # Compute initial F(0)
        F = sum(i * nums[i] for i in range(n))
        max_value = F
        
        # Compute F(k) using the derived formula
        for k in range(1, n):
            F += total_sum - n * nums[n - k]
            max_value = max(max_value, F)
        
        return max_value
