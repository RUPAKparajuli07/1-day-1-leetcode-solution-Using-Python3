# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0  # to track the maximum diameter

        def dfs(node):
            if not node:
                return 0  # return height = 0 if node is None
            
            # Get height of left and right subtrees
            left = dfs(node.left)
            right = dfs(node.right)

            # Update max_diameter with longest path through this node
            self.max_diameter = max(self.max_diameter, left + right)

            # Return the height of the current node
            return 1 + max(left, right)

        dfs(root)
        return self.max_diameter
