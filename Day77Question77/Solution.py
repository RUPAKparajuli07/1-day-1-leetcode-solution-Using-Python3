from typing import List

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def backtrack(start: int, path: List[int]):
            # If the combination is done
            if len(path) == k:
                res.append(path[:])
                return
            # Add more elements to the current combination
            for i in range(start, n + 1):
                path.append(i)
                backtrack(i + 1, path)
                path.pop()  # Backtrack

        res = []
        backtrack(1, [])
        return res

# Example usage:
sol = Solution()
print(sol.combine(4, 2))  # Output: [[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]]
print(sol.combine(1, 1))  # Output: [[1]]
