from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        n = len(nums)
        
        for i in range(n):
            if i > max_reachable:
                return False
            
            max_reachable = max(max_reachable, i + nums[i])
            
            if max_reachable >= n - 1:
                return True
        
        return False

# Example usage:
solution = Solution()
print(solution.canJump([2,3,1,1,4]))  # Output: True
print(solution.canJump([3,2,1,0,4]))  # Output: False
