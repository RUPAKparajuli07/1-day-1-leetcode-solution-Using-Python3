from typing import List

class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        
        # Step 1: Sort the array
        nums.sort()
        n = len(nums)
        
        # Step 2: Initialize DP and parent arrays
        dp = [1] * n  # dp[i] stores the size of the largest subset ending at index i
        parent = [-1] * n  # To track the previous index in the subset
        max_size = 0
        max_index = -1
        
        # Step 3: Fill DP array
        for i in range(n):
            for j in range(i):
                if nums[i] % nums[j] == 0 and dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    parent[i] = j
            
            # Update the maximum subset size and its index
            if dp[i] > max_size:
                max_size = dp[i]
                max_index = i
        
        # Step 4: Reconstruct the largest subset
        result = []
        while max_index != -1:
            result.append(nums[max_index])
            max_index = parent[max_index]
        
        return result[::-1]  # Reverse to get the subset in ascending order
