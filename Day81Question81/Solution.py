from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if nums[mid] == target:
                return True
            
            # When we cannot determine the sorted part due to duplicates
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            # If the left part is sorted
            elif nums[left] <= nums[mid]:
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # If the right part is sorted
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return False

# Example usage:
solution = Solution()
print(solution.search([2, 5, 6, 0, 0, 1, 2], 0))  # Output: True
print(solution.search([2, 5, 6, 0, 0, 1, 2], 3))  # Output: False
