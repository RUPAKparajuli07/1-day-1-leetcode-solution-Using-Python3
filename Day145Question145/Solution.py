class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack1 = [root]  # Stack to hold nodes
        stack2 = []  # Stack to hold the postorder traversal in reverse
        
        while stack1:
            node = stack1.pop()  # Get the current node
            stack2.append(node.val)  # Store node value in stack2
            
            # Push left and right children to stack1
            if node.left:
                stack1.append(node.left)
            if node.right:
                stack1.append(node.right)
        
        # The result is in reverse postorder, so reverse it
        return stack2[::-1]
