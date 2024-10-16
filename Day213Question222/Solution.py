# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        # Helper function to calculate the tree height
        def get_height(node):
            height = 0
            while node:
                height += 1
                node = node.left
            return height
        
        # Base case: if the tree is empty
        if not root:
            return 0
        
        # Get the height of the left and right subtrees
        left_height = get_height(root.left)
        right_height = get_height(root.right)
        
        # If the left and right subtree heights are the same, the left subtree is a perfect tree
        if left_height == right_height:
            # Calculate nodes in the left subtree and recurse on the right
            return (1 << left_height) + self.countNodes(root.right)
        else:
            # If heights are different, the right subtree is perfect
            # Calculate nodes in the right subtree and recurse on the left
            return (1 << right_height) + self.countNodes(root.left)
