# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        def helper(node):
            nonlocal max_sum
            if not node:
                return 0
            
            # Compute the maximum path sum starting from the left child
            left_gain = max(helper(node.left), 0)
            
            # Compute the maximum path sum starting from the right child
            right_gain = max(helper(node.right), 0)
            
            # Calculate the price of the new path which includes the current node
            price_newpath = node.val + left_gain + right_gain
            
            # Update the global maximum sum if the new path is better
            max_sum = max(max_sum, price_newpath)
            
            # For the recursion, return the maximum gain if the current node is part of the path
            return node.val + max(left_gain, right_gain)
        
        max_sum = float('-inf')
        helper(root)
        return max_sum
