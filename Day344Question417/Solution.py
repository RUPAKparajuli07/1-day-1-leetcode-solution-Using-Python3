from typing import List

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights or not heights[0]:
            return []

        rows, cols = len(heights), len(heights[0])
        pacific = set()
        atlantic = set()

        # DFS function to mark reachable cells
        def dfs(r, c, visited, prev_height):
            if ((r, c) in visited or
                r < 0 or c < 0 or r >= rows or c >= cols or
                heights[r][c] < prev_height):
                return
            visited.add((r, c))
            directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
            for dr, dc in directions:
                dfs(r + dr, c + dc, visited, heights[r][c])

        # Start DFS from Pacific (top row and left column)
        for c in range(cols):
            dfs(0, c, pacific, heights[0][c])  # Top row
            dfs(rows - 1, c, atlantic, heights[rows - 1][c])  # Bottom row

        for r in range(rows):
            dfs(r, 0, pacific, heights[r][0])  # Left column
            dfs(r, cols - 1, atlantic, heights[r][cols - 1])  # Right column

        # Find the intersection of both ocean-reachable cells
        return list(pacific & atlantic)
