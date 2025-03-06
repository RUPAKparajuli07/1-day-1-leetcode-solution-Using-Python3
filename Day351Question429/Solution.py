from collections import deque
from typing import List, Optional

# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        
        result = []
        queue = deque([root])  # Initialize queue with the root node
        
        while queue:
            level_size = len(queue)
            level_values = []
            
            for _ in range(level_size):  # Process all nodes at the current level
                node = queue.popleft()   # Remove from front of queue
                level_values.append(node.val)  # Add node value to level list
                
                for child in node.children:  # Add all children to the queue
                    queue.append(child)
            
            result.append(level_values)  # Store level values in result
        
        return result
