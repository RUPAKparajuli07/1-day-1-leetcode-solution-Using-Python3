class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        total_sum = 0
        
        # Check if the left child is a leaf
        if root.left and not root.left.left and not root.left.right:
            total_sum += root.left.val
        
        # Recurse for left and right subtrees
        total_sum += self.sumOfLeftLeaves(root.left)
        total_sum += self.sumOfLeftLeaves(root.right)
        
        return total_sum
