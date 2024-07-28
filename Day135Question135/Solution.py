from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n
        
        # Left-to-Right Pass
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        
        # Right-to-Left Pass
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)
        
        # Sum up the candies
        return sum(candies)

# Example usage:
solution = Solution()
print(solution.candy([1, 0, 2]))  # Output: 5
print(solution.candy([1, 2, 2]))  # Output: 4
