# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        # The first element in preorder is the root
        root_val = preorder[0]
        root = TreeNode(root_val)
        
        # Find the index of the root in inorder list
        mid = inorder.index(root_val)
        
        # Recursively construct the left and right subtree
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
        
        return root
