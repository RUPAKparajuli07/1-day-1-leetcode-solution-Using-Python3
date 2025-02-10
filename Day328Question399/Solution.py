from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        # Build the graph: dictionary of nodes to its neighbors and the ratio value
        graph = defaultdict(dict)
        
        # Add equations to the graph
        for (a, b), value in zip(equations, values):
            graph[a][b] = value
            graph[b][a] = 1 / value
        
        # Function to perform DFS search
        def dfs(start, end, visited):
            # If the start and end are the same, the answer is 1
            if start == end:
                return 1.0
            visited.add(start)
            # Explore neighbors
            for neighbor, ratio in graph[start].items():
                if neighbor not in visited:
                    result = dfs(neighbor, end, visited)
                    if result != -1.0:
                        return ratio * result
            return -1.0
        
        # Result for each query
        result = []
        
        for a, b in queries:
            # If either a or b is not in the graph, return -1.0
            if a not in graph or b not in graph:
                result.append(-1.0)
            else:
                result.append(dfs(a, b, set()))
        
        return result
