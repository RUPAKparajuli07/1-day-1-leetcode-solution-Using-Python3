# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        # Initialize a stack to keep track of the nodes
        self.stack = []
        # Start with pushing all the left nodes to the stack
        self._push_left_nodes(root)

    def _push_left_nodes(self, node: Optional[TreeNode]):
        """
        Helper function to push all the left children of a node onto the stack.
        """
        while node:
            self.stack.append(node)
            node = node.left

    def next(self) -> int:
        """
        Return the next smallest element in the BST.
        """
        # Pop the top element from the stack
        node = self.stack.pop()
        # If the node has a right child, push all its left children to the stack
        if node.right:
            self._push_left_nodes(node.right)
        # Return the value of the current node
        return node.val

    def hasNext(self) -> bool:
        """
        Return whether there is a next smallest number.
        """
        # Check if there are elements in the stack
        return len(self.stack) > 0

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
