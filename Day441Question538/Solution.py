# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.sum = 0  # This keeps track of the running total

        def reverse_inorder(node):
            if not node:
                return
            
            # Visit right subtree first
            reverse_inorder(node.right)
            
            # Update the node's value
            self.sum += node.val
            node.val = self.sum
            
            # Visit left subtree
            reverse_inorder(node.left)
        
        reverse_inorder(root)
        return root
