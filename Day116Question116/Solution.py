class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        # Start with the root of the tree
        leftmost = root

        while leftmost.left:
            # Iterate the "linked list" at the current level using `head`
            head = leftmost
            while head:
                # Connect the children of head node
                head.left.next = head.right
                
                # Connect the right child to the next left child (if not the last node)
                if head.next:
                    head.right.next = head.next.left
                
                # Move to the next node in the current level
                head = head.next
            
            # Move to the leftmost node in the next level
            leftmost = leftmost.left
        
        return root
