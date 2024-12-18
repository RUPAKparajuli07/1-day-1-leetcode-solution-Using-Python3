from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head  # If there are 0 or 1 nodes, no reordering needed.
        
        odd = head  # Start with the first node as odd.
        even = head.next  # The second node is even.
        even_head = even  # Save the head of the even list.

        # Iterate and rearrange nodes.
        while even and even.next:
            odd.next = even.next  # Connect the odd nodes.
            odd = odd.next  # Move odd pointer.
            even.next = odd.next  # Connect the even nodes.
            even = even.next  # Move even pointer.

        odd.next = even_head  # Append the even list after the odd list.
        return head
