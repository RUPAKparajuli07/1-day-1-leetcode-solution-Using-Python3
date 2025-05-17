from collections import Counter
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        count = Counter()

        # Helper function to calculate subtree sums
        def dfs(node):
            if not node:
                return 0
            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = node.val + left_sum + right_sum
            count[subtree_sum] += 1
            return subtree_sum

        dfs(root)

        max_freq = max(count.values())
        return [s for s in count if count[s] == max_freq]
