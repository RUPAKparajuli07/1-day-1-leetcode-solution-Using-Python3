from typing import List

class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        m, n = len(matrix), len(matrix[0])
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
        memo = [[-1] * n for _ in range(m)]  # Memoization table

        def dfs(x, y):
            if memo[x][y] != -1:
                return memo[x][y]

            max_length = 1  # Minimum path length is 1 (current cell)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and matrix[nx][ny] > matrix[x][y]:
                    max_length = max(max_length, 1 + dfs(nx, ny))

            memo[x][y] = max_length
            return max_length

        # Compute the longest path for each cell
        longest_path = 0
        for i in range(m):
            for j in range(n):
                longest_path = max(longest_path, dfs(i, j))

        return longest_path
