from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(city):
            visited[city] = True
            for neighbor in range(len(isConnected)):
                # If connected and not yet visited
                if isConnected[city][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)

        n = len(isConnected)
        visited = [False] * n
        provinces = 0

        for i in range(n):
            if not visited[i]:
                dfs(i)
                provinces += 1  # Every DFS call means one new province

        return provinces
