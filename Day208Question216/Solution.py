from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # Helper function to perform the backtracking
        def backtrack(start, remaining, path):
            # Base case: if we have exactly k numbers and the sum is n
            if len(path) == k and remaining == 0:
                result.append(path[:])
                return
            # If the sum exceeds or we have too many numbers, stop further exploration
            if len(path) > k or remaining < 0:
                return
            
            # Explore the numbers from 'start' to 9
            for i in range(start, 10):
                # Add current number to the combination and explore further
                path.append(i)
                backtrack(i + 1, remaining - i, path)
                # Remove the last added number to backtrack and try another combination
                path.pop()

        result = []
        backtrack(1, n, [])
        return result
