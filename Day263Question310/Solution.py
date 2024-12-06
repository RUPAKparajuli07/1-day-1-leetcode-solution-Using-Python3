from collections import deque, defaultdict
from typing import List

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # If there's only one node, it's the root of the MHT
        if n == 1:
            return [0]
        
        # Step 1: Build the adjacency list for the graph
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: BFS to find the farthest node from any node (start with node 0)
        def bfs(start: int) -> (int, List[int]):
            visited = [-1] * n
            visited[start] = 0
            q = deque([start])
            farthest_node = start
            max_distance = 0
            
            while q:
                node = q.popleft()
                for neighbor in graph[node]:
                    if visited[neighbor] == -1:  # not visited
                        visited[neighbor] = visited[node] + 1
                        q.append(neighbor)
                        if visited[neighbor] > max_distance:
                            max_distance = visited[neighbor]
                            farthest_node = neighbor
            return farthest_node, visited
        
        # Step 3: Find the two endpoints of the diameter
        # First BFS to find one endpoint of the diameter
        farthest_node_from_start, _ = bfs(0)
        
        # Second BFS to find the other endpoint of the diameter
        other_end, distances = bfs(farthest_node_from_start)
        
        # Step 4: Trace back to find the centers of the tree
        path = []
        node = other_end
        while node != farthest_node_from_start:
            path.append(node)
            # Move to the previous node in the path
            for neighbor in graph[node]:
                if distances[neighbor] == distances[node] - 1:
                    node = neighbor
                    break
        path.append(farthest_node_from_start)
        
        # Step 5: The center(s) of the diameter are the minimum height tree roots
        # If the path length is odd, there's one center, otherwise there are two centers
        path_length = len(path)
        if path_length % 2 == 1:
            return [path[path_length // 2]]
        else:
            return [path[path_length // 2 - 1], path[path_length // 2]]

