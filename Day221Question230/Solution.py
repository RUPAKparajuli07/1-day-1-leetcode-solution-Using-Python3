# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # In-order traversal helper function
        def inorder(node):
            if node is None:
                return
            # Traverse left subtree
            yield from inorder(node.left)
            # Visit the current node
            yield node.val
            # Traverse right subtree
            yield from inorder(node.right)

        # Generator for in-order traversal
        gen = inorder(root)
        # Extract the kth element from the generator
        for _ in range(k):
            result = next(gen)
        return result
