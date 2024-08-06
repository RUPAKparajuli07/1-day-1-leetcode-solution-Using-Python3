class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        
        stack, result = [root], []
        
        while stack:
            node = stack.pop()
            if node:
                # Visit root
                result.append(node.val)
                # Push right and then left child to the stack
                if node.right:
                    stack.append(node.right)
                if node.left:
                    stack.append(node.left)
        
        return result
