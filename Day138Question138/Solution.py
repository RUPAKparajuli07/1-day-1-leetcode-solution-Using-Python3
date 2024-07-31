class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        # Step 1: Interweave original and copied nodes
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        
        # Step 2: Assign random pointers to the new nodes
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        
        # Step 3: Separate the original and copied lists
        old_list = head
        new_list = head.next
        new_head = head.next
        
        while old_list:
            old_list.next = old_list.next.next
            if new_list.next:
                new_list.next = new_list.next.next
            old_list = old_list.next
            new_list = new_list.next
        
        return new_head
