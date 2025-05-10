from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [-1] * n  # Default value is -1
        stack = []  # This will store indices, not values

        # Loop through the array twice to simulate circular behavior
        for i in range(2 * n - 1, -1, -1):
            current = nums[i % n]
            
            # Maintain decreasing stack: pop smaller or equal elements
            while stack and nums[stack[-1]] <= current:
                stack.pop()
            
            # Only update result in the first pass
            if i < n:
                if stack:
                    result[i] = nums[stack[-1]]
                # else: result[i] already set to -1
            
            # Push current index to stack
            stack.append(i % n)

        return result
