# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import List, Optional

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        def dfs(node, path, paths):
            if not node:
                return
            # Append current node's value to the path
            path += str(node.val)
            
            # If it's a leaf node, add path to results
            if not node.left and not node.right:
                paths.append(path)
            else:
                # Extend path for next children
                path += "->"
                dfs(node.left, path, paths)
                dfs(node.right, path, paths)
        
        paths = []
        dfs(root, "", paths)
        return paths
