from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Base case: if either array is empty, return None
        if not inorder or not postorder:
            return None
        
        # The last element in postorder is the root
        root_val = postorder.pop()
        root = TreeNode(root_val)
        
        # Find the root in inorder to divide left and right subtrees
        inorder_index = inorder.index(root_val)
        
        # Recursively build the right subtree and then the left subtree
        # It's important to build the right subtree first because we are using the last element in postorder
        root.right = self.buildTree(inorder[inorder_index + 1:], postorder)
        root.left = self.buildTree(inorder[:inorder_index], postorder)
        
        return root
