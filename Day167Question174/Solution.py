from typing import List

class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m, n = len(dungeon), len(dungeon[0])
        
        # Initialize a DP table with 'inf' values
        dp = [[float('inf')] * (n + 1) for _ in range(m + 1)]
        
        # Minimum health needed to survive in the princess room or just beyond
        dp[m][n - 1] = dp[m - 1][n] = 1
        
        # Fill the DP table in reverse order
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                # Minimum health needed to move right or down
                min_health_on_exit = min(dp[i + 1][j], dp[i][j + 1])
                # Compute the minimum health required at (i, j)
                dp[i][j] = max(min_health_on_exit - dungeon[i][j], 1)
        
        return dp[0][0]
