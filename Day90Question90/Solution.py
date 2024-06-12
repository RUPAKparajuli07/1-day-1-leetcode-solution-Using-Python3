from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            result.append(path[:])
            for i in range(start, len(nums)):
                # Skip duplicates
                if i > start and nums[i] == nums[i - 1]:
                    continue
                # Include nums[i] in the subset
                path.append(nums[i])
                # Move to the next element
                backtrack(i + 1, path)
                # Backtrack by removing the last element
                path.pop()
        
        # Sort the array to handle duplicates
        nums.sort()
        result = []
        backtrack(0, [])
        return result

# Example usage
solution = Solution()
print(solution.subsetsWithDup([1, 2, 2]))  # Output: [[], [1], [1, 2], [1, 2, 2], [2], [2, 2]]
print(solution.subsetsWithDup([0]))  # Output: [[], [0]]
