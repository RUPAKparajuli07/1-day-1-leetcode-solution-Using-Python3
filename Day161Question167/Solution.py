from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1  # Initialize two pointers
        
        while left < right:
            current_sum = numbers[left] + numbers[right]  # Calculate the current sum
            
            if current_sum == target:
                return [left + 1, right + 1]  # Return the 1-based indices
            
            elif current_sum < target:
                left += 1  # Move the left pointer to the right to increase the sum
                
            else:
                right -= 1  # Move the right pointer to the left to decrease the sum

# Example usage:
solution = Solution()
print(solution.twoSum([2, 7, 11, 15], 9))  # Output: [1, 2]
print(solution.twoSum([2, 3, 4], 6))       # Output: [1, 3]
print(solution.twoSum([-1, 0], -1))        # Output: [1, 2]
