from typing import List

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = set()  # Use set to avoid duplicate subsequences
        
        def backtrack(start: int, path: List[int]):
            if len(path) >= 2:
                result.add(tuple(path))  # Convert list to tuple to store in set
                
            for i in range(start, len(nums)):
                if not path or nums[i] >= path[-1]:  # If path is empty or non-decreasing
                    backtrack(i + 1, path + [nums[i]])  # Choose nums[i]
        
        backtrack(0, [])
        return list(map(list, result))  # Convert tuples back to lists

