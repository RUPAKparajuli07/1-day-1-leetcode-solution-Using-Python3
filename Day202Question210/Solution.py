from collections import defaultdict, deque
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Step 1: Create the graph and indegree array
        graph = defaultdict(list)  # Adjacency list for graph
        indegree = [0] * numCourses  # Indegree of each course
        
        # Step 2: Build the graph and fill indegree
        for course, pre in prerequisites:
            graph[pre].append(course)
            indegree[course] += 1
        
        # Step 3: Initialize queue with courses having indegree 0 (no prerequisites)
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        result = []
        
        # Step 4: Process the queue for topological sorting
        while queue:
            course = queue.popleft()  # Take course with no remaining prerequisites
            result.append(course)
            
            # Decrease the indegree of neighboring courses
            for neighbor in graph[course]:
                indegree[neighbor] -= 1
                # If indegree becomes 0, it can now be taken
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Step 5: Check if we processed all courses
        if len(result) == numCourses:
            return result
        else:
            return []  # Cycle detected, impossible to finish all courses
