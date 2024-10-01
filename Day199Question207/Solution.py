from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Create an adjacency list to represent the graph
        graph = [[] for _ in range(numCourses)]
        for course, prereq in prerequisites:
            graph[prereq].append(course)  # To take course, need to finish prereq first
        
        # Step 2: Create a list to track visited nodes
        visited = [0] * numCourses  # 0: unvisited, 1: visiting, 2: visited
        
        # Step 3: DFS function to check for cycles
        def dfs(course):
            if visited[course] == 1:  # cycle detected
                return False
            if visited[course] == 2:  # already checked and no cycle
                return True
            
            visited[course] = 1  # mark as visiting
            for next_course in graph[course]:
                if not dfs(next_course):  # cycle found in the recursive call
                    return False
            
            visited[course] = 2  # mark as visited
            return True
        
        # Step 4: Check each course
        for i in range(numCourses):
            if not dfs(i):  # if any course results in a cycle, return False
                return False
        
        return True  # no cycles detected, so return True

# Example Usage
solution = Solution()
print(solution.canFinish(2, [[1, 0]]))  # Output: True
print(solution.canFinish(2, [[1, 0], [0, 1]]))  # Output: False
