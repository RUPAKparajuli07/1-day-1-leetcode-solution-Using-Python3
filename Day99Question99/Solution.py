# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # Initialize pointers for the nodes to be swapped
        first_element = second_element = None
        # Previous element pointer
        prev_element = TreeNode(float('-inf'))
        
        def in_order_traversal(node: Optional[TreeNode]):
            nonlocal first_element, second_element, prev_element
            
            if not node:
                return
            
            # In-order traversal: Left -> Node -> Right
            in_order_traversal(node.left)
            
            # If we find an anomaly (previous node value > current node value)
            if prev_element.val >= node.val:
                # If it's the first anomaly, mark both first_element and second_element
                if not first_element:
                    first_element = prev_element
                # If it's the second anomaly, mark second_element
                second_element = node
            
            # Update the previous node pointer
            prev_element = node
            
            in_order_traversal(node.right)
        
        # Perform in-order traversal to find the two elements
        in_order_traversal(root)
        
        # Swap the values of the first and second elements
        if first_element and second_element:
            first_element.val, second_element.val = second_element.val, first_element.val
