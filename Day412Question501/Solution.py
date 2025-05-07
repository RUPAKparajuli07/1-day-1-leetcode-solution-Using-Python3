# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        self.current_val = None
        self.current_count = 0
        self.max_count = 0
        self.modes = []

        def in_order(node):
            if not node:
                return
            
            # Traverse left subtree
            in_order(node.left)
            
            # Process current node
            if node.val != self.current_val:
                self.current_val = node.val
                self.current_count = 1
            else:
                self.current_count += 1

            # Update modes list
            if self.current_count > self.max_count:
                self.max_count = self.current_count
                self.modes = [self.current_val]
            elif self.current_count == self.max_count:
                self.modes.append(self.current_val)
            
            # Traverse right subtree
            in_order(node.right)

        in_order(root)
        return self.modes
