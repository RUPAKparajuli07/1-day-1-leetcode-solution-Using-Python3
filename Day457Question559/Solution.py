# Definition for a Node.
class Node:
    def __init__(self, val: int = None, children: list['Node'] = None):
        self.val = val
        self.children = children if children is not None else []

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        
        # If no children, depth is 1 (just the root)
        if not root.children:
            return 1

        # Recursively calculate the depth of each subtree and take the max
        max_child_depth = max(self.maxDepth(child) for child in root.children)
        return 1 + max_child_depth
