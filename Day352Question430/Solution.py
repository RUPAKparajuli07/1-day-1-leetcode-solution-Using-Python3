class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        
        stack = []  # Stack to keep track of nodes
        curr = head
        
        while curr:
            if curr.child:
                # If there is a next node, push it onto the stack
                if curr.next:
                    stack.append(curr.next)
                
                # Connect current node to child and remove child pointer
                curr.next = curr.child
                curr.child.prev = curr
                curr.child = None
            
            # If we reach the end of the current level and there are nodes in stack
            if not curr.next and stack:
                next_node = stack.pop()
                curr.next = next_node
                next_node.prev = curr
            
            curr = curr.next
        
        return head
