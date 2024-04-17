from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left

        def find_right(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    left = mid + 1
                else:
                    right = mid - 1
            return right

        left_idx = find_left(nums, target)
        right_idx = find_right(nums, target)

        if left_idx <= right_idx:
            return [left_idx, right_idx]
        else:
            return [-1, -1]

# Example usage:
nums = [5, 7, 7, 8, 8, 10]
target = 8
solution = Solution()
print(solution.searchRange(nums, target))  # Output: [3, 4]
