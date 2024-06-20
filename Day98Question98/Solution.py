# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        def validate(node, low=-float('inf'), high=float('inf')):
            # An empty tree is a valid BST
            if not node:
                return True
            # The current node's value must be between the low and high values
            if node.val <= low or node.val >= high:
                return False
            # Recursively check the subtrees with updated ranges
            return (validate(node.left, low, node.val) and
                    validate(node.right, node.val, high))
        
        return validate(root)

# Example usage:
# root = TreeNode(2, TreeNode(1), TreeNode(3))
# sol = Solution()
# print(sol.isValidBST(root))  # Output: True

# root = TreeNode(5, TreeNode(1), TreeNode(4, TreeNode(3), TreeNode(6)))
# sol = Solution()
# print(sol.isValidBST(root))  # Output: False
