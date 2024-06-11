from typing import List

class Solution:
    def grayCode(self, n: int) -> List[int]:
        result = []
        for i in range(2 ** n):
            result.append(i ^ (i >> 1))
        return result

# Example usage
sol = Solution()
print(sol.grayCode(2))  # Output: [0, 1, 3, 2]
print(sol.grayCode(1))  # Output: [0, 1]
