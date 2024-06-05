class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize current node as head
        current = head
        
        # Traverse the list
        while current and current.next:
            # If the current node's value is the same as the next node's value
            if current.val == current.next.val:
                # Skip the next node
                current.next = current.next.next
            else:
                # Move to the next node
                current = current.next
        
        # Return the modified list
        return head
