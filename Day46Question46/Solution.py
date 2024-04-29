from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []
        self.permute_recursive(nums, 0, result)
        return result
    
    def permute_recursive(self, nums, start, result):
        if start == len(nums):
            result.append(nums[:])  # Make a copy of nums to avoid modifying the original list
            return
        
        for i in range(start, len(nums)):
            # Swap elements at indices start and i
            nums[start], nums[i] = nums[i], nums[start]
            # Recursively generate permutations for the rest of the array
            self.permute_recursive(nums, start + 1, result)
            # Backtrack by swapping back elements at indices start and i
            nums[start], nums[i] = nums[i], nums[start]

# Example usage:
solution = Solution()
print(solution.permute([1, 2, 3]))  # Output: [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 2, 1], [3, 1, 2]]
print(solution.permute([0, 1]))      # Output: [[0, 1], [1, 0]]
print(solution.permute([1]))         # Output: [[1]]
