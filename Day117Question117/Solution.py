class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        
        # Initialize a queue for level-order traversal
        queue = collections.deque([root])
        
        while queue:
            level_length = len(queue)
            
            for i in range(level_length):
                node = queue.popleft()
                
                # Connect the node to the next node in the queue if it is not the last node of the level
                if i < level_length - 1:
                    node.next = queue[0]
                
                # Enqueue children of the current node
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
        
        return root
