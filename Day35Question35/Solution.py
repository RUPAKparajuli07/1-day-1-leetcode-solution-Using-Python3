from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        # If the loop terminates, it means the target is not found
        # The correct position to insert the target is at 'left'
        return left

# Example usage:
solution = Solution()
nums = [1, 3, 5, 6]
print(solution.searchInsert(nums, 5))  # Output: 2
print(solution.searchInsert(nums, 2))  # Output: 1
print(solution.searchInsert(nums, 7))  # Output: 4
