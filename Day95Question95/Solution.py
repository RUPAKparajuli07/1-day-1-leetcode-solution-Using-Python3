from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []
        return self.generate_trees(1, n, {})

    def generate_trees(self, start, end, memo):
        if start > end:
            return [None]
        
        if (start, end) in memo:
            return memo[(start, end)]
        
        all_trees = []
        for i in range(start, end + 1):
            left_trees = self.generate_trees(start, i - 1, memo)
            right_trees = self.generate_trees(i + 1, end, memo)
            
            for left_tree in left_trees:
                for right_tree in right_trees:
                    root = TreeNode(i)
                    root.left = left_tree
                    root.right = right_tree
                    all_trees.append(root)
        
        memo[(start, end)] = all_trees
        return all_trees
