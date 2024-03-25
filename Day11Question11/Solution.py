from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        left = 0
        right = len(height) - 1

        while left < right:
            width = right - left
            h = min(height[left], height[right])
            max_area = max(max_area, width * h)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area

# Example usage:
height1 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(sol.maxArea(height1))  # Output: 49

height2 = [1, 1]
print(sol.maxArea(height2))  # Output: 1
