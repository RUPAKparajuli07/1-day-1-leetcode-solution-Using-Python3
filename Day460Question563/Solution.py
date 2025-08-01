# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.total_tilt = 0  # This stores the final sum of all tilts

        def dfs(node):
            if not node:
                return 0  # Base case: null nodes contribute 0 to the sum

            # Recursive calls to compute sum of left and right subtrees
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            # Compute tilt of the current node
            current_tilt = abs(left_sum - right_sum)

            # Accumulate tilt
            self.total_tilt += current_tilt

            # Return the total sum of this subtree
            return left_sum + right_sum + node.val

        dfs(root)
        return self.total_tilt
