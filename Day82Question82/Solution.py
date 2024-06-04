# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize a dummy node
        dummy = ListNode(0)
        dummy.next = head
        
        # prev is the last node before the sequence of duplicates
        prev = dummy
        
        while head:
            # If current node has a duplicate
            if head.next and head.val == head.next.val:
                # Skip all nodes with the same value
                while head.next and head.val == head.next.val:
                    head = head.next
                # Connect prev to the node after the last duplicate
                prev.next = head.next
            else:
                # No duplicates detected, move prev to head
                prev = prev.next
            # Move head to the next node
            head = head.next
        
        # Return the modified list
        return dummy.next
