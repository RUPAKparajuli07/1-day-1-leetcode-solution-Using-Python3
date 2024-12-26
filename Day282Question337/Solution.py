from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate rob and not_rob values
        def dfs(node):
            if not node:
                return (0, 0)  # Base case: (rob, not_rob)

            # Postorder traversal
            left = dfs(node.left)
            right = dfs(node.right)

            # If we rob this node, we cannot rob its children
            rob = node.val + left[1] + right[1]

            # If we don't rob this node, we can rob or not rob its children
            not_rob = max(left) + max(right)

            return (rob, not_rob)

        # Compute results starting from the root
        result = dfs(root)
        return max(result)  # Return the best option (rob or not_rob) for the root
