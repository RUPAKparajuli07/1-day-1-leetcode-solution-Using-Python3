# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Traverse the tree starting from the root
        current = root
        
        while current:
            # If both p and q are greater than current node, move to right subtree
            if p.val > current.val and q.val > current.val:
                current = current.right
            # If both p and q are less than current node, move to left subtree
            elif p.val < current.val and q.val < current.val:
                current = current.left
            else:
                # We found the split point, so this is the LCA
                return current
