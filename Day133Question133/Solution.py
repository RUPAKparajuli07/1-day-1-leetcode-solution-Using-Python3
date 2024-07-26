# Definition for a Node.
class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        
        # A dictionary to save the cloned nodes
        clone_map = {}
        
        # DFS function to clone the graph
        def dfs(node):
            if node in clone_map:
                return clone_map[node]
            
            # Clone the node
            clone = Node(node.val)
            clone_map[node] = clone
            
            # Iterate through all the neighbors to clone them
            for neighbor in node.neighbors:
                clone.neighbors.append(dfs(neighbor))
            
            return clone
        
        return dfs(node)
