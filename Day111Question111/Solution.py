from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        queue = deque([(root, 1)])  # Initialize the queue with the root node and its depth
        
        while queue:
            node, depth = queue.popleft()
            
            # Check if the node is a leaf node
            if not node.left and not node.right:
                return depth
            
            # Add the left child to the queue if it exists
            if node.left:
                queue.append((node.left, depth + 1))
            
            # Add the right child to the queue if it exists
            if node.right:
                queue.append((node.right, depth + 1))
        
        return 0  # This line will never be reached because the input tree is guaranteed to be valid

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

solution = Solution()
print(solution.minDepth(root))  # Output: 2
