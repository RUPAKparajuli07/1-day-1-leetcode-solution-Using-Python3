from collections import defaultdict
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, cumulative_sum):
            if not node:
                return 0
            
            # Update current sum
            cumulative_sum += node.val
            
            # Check if (cumulative_sum - targetSum) exists in the map
            count = prefix_sum[cumulative_sum - targetSum]
            
            # Update prefix_sum with current cumulative_sum
            prefix_sum[cumulative_sum] += 1
            
            # Recur for left and right subtrees
            count += dfs(node.left, cumulative_sum)
            count += dfs(node.right, cumulative_sum)
            
            # Backtrack: remove current cumulative_sum from the map
            prefix_sum[cumulative_sum] -= 1
            
            return count
        
        # Dictionary to store prefix sums, initialized with {0:1} for base case
        prefix_sum = defaultdict(int)
        prefix_sum[0] = 1
        
        return dfs(root, 0)
