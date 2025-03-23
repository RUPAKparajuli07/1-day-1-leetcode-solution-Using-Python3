# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque
from typing import Optional

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """
        Converts a binary tree into a string representation using level-order traversal.
        """
        if not root:
            return ""  # Return an empty string if the tree is empty
        
        queue = deque([root])  # Initialize queue for level-order traversal
        output = []  # List to store serialized values
        
        while queue:
            current = queue.popleft()  # Get the next node from the queue
            
            if current:
                output.append(str(current.val))  # Store the node value as a string
                queue.append(current.left)  # Add left child to queue
                queue.append(current.right)  # Add right child to queue
            else:
                output.append("null")  # Use "null" to represent missing children
        
        return ",".join(output)  # Convert the list into a comma-separated string

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """
        Converts a serialized string back into a binary tree using level-order reconstruction.
        """
        if not data:
            return None  # Return None if the input string is empty
        
        nodes = data.split(",")  # Split the string into a list of values
        root = TreeNode(int(nodes[0]))  # Create the root node
        queue = deque([root])  # Queue to track nodes during tree reconstruction
        i = 1  # Pointer to track position in nodes list
        
        while queue:
            current = queue.popleft()  # Get the next node from the queue
            
            # Handle left child
            if nodes[i] != "null":  # If it's not null, create a left child node
                current.left = TreeNode(int(nodes[i]))
                queue.append(current.left)  # Add left child to queue
            i += 1
            
            # Handle right child
            if nodes[i] != "null":  # If it's not null, create a right child node
                current.right = TreeNode(int(nodes[i]))
                queue.append(current.right)  # Add right child to queue
            i += 1
        
        return root  # Return the reconstructed tree

# Example usage:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)  # Convert tree to string
# ans = deser.deserialize(tree)  # Convert string back to tree
# return ans
