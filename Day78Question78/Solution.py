from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            # Append the current subset (path) to the result
            result.append(path[:])
            # Explore further elements to be added to the current subset
            for i in range(start, len(nums)):
                # Include nums[i] in the current subset
                path.append(nums[i])
                # Recurse with the next starting index
                backtrack(i + 1, path)
                # Exclude nums[i] from the current subset (backtrack)
                path.pop()
        
        result = []
        backtrack(0, [])
        return result
