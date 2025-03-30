from typing import List

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []  # Monotonic decreasing stack
        third = float('-inf')  # This will store the potential nums[k]

        # Traverse from right to left
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < third:  # Found a valid nums[i] < nums[k]
                return True
            
            while stack and stack[-1] < nums[i]:  # Find the next largest value
                third = stack.pop()  # Update third to the last popped element

            stack.append(nums[i])  # Push current element to stack
        
        return False
