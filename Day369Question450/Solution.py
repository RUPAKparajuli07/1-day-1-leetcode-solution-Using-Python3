from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None  # If the tree is empty or key not found
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)  # Search in the left subtree
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)  # Search in the right subtree
        else:
            # Node with the key found
            
            # Case 1: Node has no child or only one child
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # Case 2: Node has two children
            successor = self.getMin(root.right)  # Find the inorder successor
            root.val = successor.val  # Replace value with successor
            root.right = self.deleteNode(root.right, successor.val)  # Delete successor
        
        return root

    def getMin(self, node: TreeNode) -> TreeNode:
        """Find the smallest node in the right subtree (inorder successor)."""
        while node.left:
            node = node.left
        return node
