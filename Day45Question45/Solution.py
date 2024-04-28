from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) <= 1:  # If there is only one element or no element, no need to jump
            return 0
        
        max_reach = nums[0]  # Maximum index you can reach from the current position
        steps = nums[0]  # Number of steps you can still take
        jumps = 1  # Number of jumps needed
        
        for i in range(1, len(nums)):
            if i == len(nums) - 1:  # If we reached the last index
                return jumps
            
            max_reach = max(max_reach, i + nums[i])  # Update the maximum index you can reach
            
            steps -= 1  # We took a step
            
            if steps == 0:  # If we can't take any more steps from the current position
                jumps += 1  # We need to jump
                steps = max_reach - i  # Update steps to the maximum index we can reach from the current position minus the current index
                
        return jumps

# Test cases
sol = Solution()
print(sol.jump([2,3,1,1,4]))  # Output: 2
print(sol.jump([2,3,0,1,4]))  # Output: 2
